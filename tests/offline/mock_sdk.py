"""Tiny offline fake GenLayer surface for deterministic invariants only.

Not GenVM, not Direct Mode, and NOT proof of validator runtime compatibility.
Never use this to certify live consensus.
"""

import importlib.util
import sys
import types
from pathlib import Path


class MockUserError(Exception):
    pass


class MockAddress(str):
    @property
    def as_hex(self):
        return str(self)


class MockTreeMap(dict):
    @classmethod
    def __class_getitem__(cls, _):
        return cls


class MockContract:
    def __getattr__(self, name):
        if name in type(self).__annotations__:
            value = 0 if name == "case_count" else MockTreeMap()
            object.__setattr__(self, name, value)
            return value
        raise AttributeError(name)


class MockResult:
    @classmethod
    def __class_getitem__(cls, _):
        return cls


class MockReturn(MockResult):
    def __init__(self, calldata):
        self.calldata = calldata


class MockVM:
    UserError = MockUserError
    Result = MockResult
    Return = MockReturn

    def __init__(self):
        self.responses = []
        self.proposal = None
        self.last_validator = None

    def set_responses(self, *responses):
        self.responses = list(responses)

    def run_nondet(self, leader_fn, validator_fn):
        self.last_validator = validator_fn
        self.proposal = leader_fn()
        if not validator_fn(MockReturn(self.proposal)):
            raise MockUserError("VALIDATOR_DISAGREEMENT")
        return self.proposal


class OfflineEnvironment:
    def __init__(self, contract_path: Path):
        self.vm = MockVM()
        self.message = types.SimpleNamespace(
            sender_address=MockAddress("0x" + "a" * 40)
        )

        self.gl = types.ModuleType("genlayer")
        self.gl.contract = types.SimpleNamespace(Contract=MockContract)
        self.gl.storage = types.SimpleNamespace(TreeMap=MockTreeMap)
        self.gl.vm = self.vm
        self.gl.message = self.message
        self.gl.public = types.SimpleNamespace(
            view=lambda fn: fn,
            write=lambda fn: fn,
        )
        self.gl.nondet = types.SimpleNamespace(exec_prompt=self._prompt)

        typed = types.ModuleType("genlayer.types")
        typed.Address = MockAddress
        typed.u64 = int
        typed.u32 = int
        typed.__all__ = ["Address", "u64", "u32"]
        self.typed = typed

        sys.modules["genlayer"] = self.gl
        sys.modules["genlayer.types"] = typed
        spec = importlib.util.spec_from_file_location(
            "proof_weave_contract_offline", contract_path
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.module = module
        self.contract = module.ProofWeave()

    def _prompt(self, _prompt, response_format):
        if response_format != "json":
            raise AssertionError("unexpected format")
        if not self.vm.responses:
            raise AssertionError("unexpected LLM call")
        val = self.vm.responses.pop(0)
        if isinstance(val, Exception):
            raise val
        return val

    def sender(self, letter):
        self.message.sender_address = MockAddress("0x" + letter * 40)

    @staticmethod
    def outcomes(a, b):
        return {"outcomes": [a, b]}
