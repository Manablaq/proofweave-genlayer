# ProofWeave — evidence-based claim resolution on GenLayer

ProofWeave is a **standalone GenLayer Intelligent Contract** that collects two independent on-chain witness submissions about a claim, applies an AI-assisted classification under GenLayer consensus, and records a case decision. There is no frontend in this release.

## Verified live demonstration

| Field | Result |
|---|---|
| Network | GenLayer Studio Devnet, chain ID `61997` |
| Contract | `0x180ffF4454836E367061957A0E4440Cfc0509B80` |
| Case | `case:1` |
| Evidence | Two distinct witness addresses and source references |
| Witness C transaction | `0xa1136c6bc833f2b84c4561ef224ac6418ada9b4432df325bf859da6fb69a4857` |
| Witness D transaction | `0x04e63362277377af0118500a639f04bc7ada62cfadbce9a6201bdbcef92c42d8` |
| Resolution transaction | `0x4752b55999ef9b68bcffc9e49f0b1157d1a92c22e59781e12ee4c0c8c4de9820` |
| All three consensus outcomes | `FINALIZED` / `MAJORITY_AGREE` |
| Final case state | `RESOLVED`, `evidence_count=2` |
| Final classification | `SS` → `CORROBORATED` |
| Deployed source SHA-256 | `a57384aeb9140eda87f8b593adc697343370ae504ca6f37d30c54cefded50d7f` |

**Source provenance:** `contracts/proof_weave.py` in this prepared release is copied from the SHA-verified `deployed_proof_weave.py` in the sanitized reviewer certificate, not from the slightly different local working copy. Its hash must equal the deployed source hash above.

## How it works

1. A creator calls `create_case(claim, parent_case_id)`, producing `case:N` in `COLLECTING` state.
2. Two distinct non-creator addresses call `submit_evidence(case_id, source_ref, witness_text)`. The contract rejects a reused witness and a reused source reference.
3. Once the second evidence is accepted, the case is `READY`.
4. `resolve_case(case_id)` runs GenLayer's nondeterministic evidence classification and validator comparison, saves the two-character vector, and records `CORROBORATED`, `CONFLICTED`, or `UNPROVEN` with `RESOLVED` status.
5. `get_case`, `get_evidence`, `get_case_count`, `get_limits`, and `version` expose public views.

## Reproducible review

See [`docs/LIVE_VERIFICATION.md`](docs/LIVE_VERIFICATION.md) for the exact three transaction hashes and read-only verification procedure, [`docs/TEST_REPORT.md`](docs/TEST_REPORT.md) for tested scope, and [`docs/REVIEWER_NOTES.md`](docs/REVIEWER_NOTES.md) for candid limitations.

Sanitized archived proof is in [`docs/evidence/`](docs/evidence/), including `final_case_certificate.json`, `evidence_manifest.json`, and `REVIEWER_EVIDENCE.md`. It is a **digest** of original RPC records, not a substitute for the original raw observations (retained privately by the author).

## Important limitations

The sample claim and witness reports are **synthetic test data**. ProofWeave classifies the relation between submitted statements and a claim; it **does not independently authenticate external sources or establish real-world truth**. The completed live demo proves only `SS → CORROBORATED`. Live finality for `CONFLICTED` and `UNPROVEN`, abuse paths, revision paths, and production networks is **not claimed**. Reviewer acceptance and public-repo provenance are separate from on-chain finality.
