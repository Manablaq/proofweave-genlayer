# Case 1 — live-network verification

**Network:** Studio Devnet (chain 61997). **Contract:** `0x180ffF4454836E367061957A0E4440Cfc0509B80`.

## Finalized transactions

| Action | Transaction hash | Consensus |
|---|---|---|
| Witness C: `submit_evidence` | `0xa1136c6bc833f2b84c4561ef224ac6418ada9b4432df325bf859da6fb69a4857` | `FINALIZED` / `MAJORITY_AGREE` |
| Witness D: `submit_evidence` | `0x04e63362277377af0118500a639f04bc7ada62cfadbce9a6201bdbcef92c42d8` | `FINALIZED` / `MAJORITY_AGREE` |
| Creator: `resolve_case("case:1")` | `0x4752b55999ef9b68bcffc9e49f0b1157d1a92c22e59781e12ee4c0c8c4de9820` | `FINALIZED` / `MAJORITY_AGREE` |

## Read-only verification procedure

1. On the Studio Devnet JSON-RPC endpoint `https://studio-dev.genlayer.com/api`, call `eth_chainId` and require `61997`.
2. For each transaction hash, call `gen_getTransactionStatusDetails` and verify `status=FINALIZED` (the observed code was 7); call `eth_getTransactionByHash` and verify the consensus result `MAJORITY_AGREE`. The `eth_getTransactionReceipt` response alone is **not** a GenLayer finality proof.
3. Read the deployed ProofWeave contract's `get_case("case:1")` view using GenLayer's contract-call encoding. Confirm `status=RESOLVED`, `evidence_count=2`, `vector=SS`, and `decision=CORROBORATED`. Confirm the `resolved_by` field equals `0x1f87ae197af539253978d435ad45ccf28fb95024`.
4. Read `get_evidence("case:1", 1)` and `get_evidence("case:1", 2)`. Verify the two witnesses and two source references differ. Witness source refs are `synthetic:proofweave/case-1/witness-c/demo-42` and `synthetic:proofweave/case-1/witness-d/demo-42`.
5. Compare the observations against `docs/evidence/final_case_certificate.json`, `docs/evidence/REVIEWER_EVIDENCE.md`, and `docs/evidence/evidence_manifest.json`.

The original 11 RPC responses were independently hash-verified during the finality certification on October 18, 2026. The shareable certificate lists their SHA-256 hashes, but excludes the raw response bytes and signed transactions. Raw evidence remains with the author and can be supplied for separate review if appropriate.

The deployed source is `contracts/proof_weave.py` with SHA-256 `a57384aeb9140eda87f8b593adc697343370ae504ca6f37d30c54cefded50d7f`. The working copy had only comment-level differences confirmed AST-equivalent; reviewers should use the **exact deployed snapshot** bundled here.
