# ProofWeave — Case 1 final live lifecycle evidence certificate

**Certification scope:** one completed *synthetic* positive-path case, Studio Devnet (chain 61997). This is a verified offline digest of previously archived RPC evidence, not a new live RPC query and not an independent production audit.

## Verified result

| Field | Final state |
| --- | --- |
| Intelligent Contract | `0x180ffF4454836E367061957A0E4440Cfc0509B80` |
| Case | `case:1` |
| Case status | **RESOLVED** |
| Evidence count | **2** (distinct witnesses and source refs) |
| Classification vector | **SS** |
| Classifier decision | **CORROBORATED** |
| Resolver | `0x1f87ae197af539253978d435ad45ccf28fb95024` |
| Witness C transaction | `0xa1136c6bc833f2b84c4561ef224ac6418ada9b4432df325bf859da6fb69a4857` |
| Witness D transaction | `0x04e63362277377af0118500a639f04bc7ada62cfadbce9a6201bdbcef92c42d8` |
| Resolution transaction | `0x4752b55999ef9b68bcffc9e49f0b1157d1a92c22e59781e12ee4c0c8c4de9820` |
| Each transaction consensus | **FINALIZED / MAJORITY_AGREE** |
| Resolution transaction receipt | **SUCCESS** |
| Original signed resolution raw file | **SHA-256 verified, NOT copied** |
| Deployed source SHA-256 | `a57384aeb9140eda87f8b593adc697343370ae504ca6f37d30c54cefded50d7f` |
| Source AST equivalence with local source | **PASS** |
| Strict Direct Mode test log | **HASH_VERIFIED** |

## Evidence provenance

The original 11 persisted RPC responses were verified byte-for-byte against SHA-256 values captured in the finality run. The original resolution signing intent, exact fee quote, exclusive one-attempt marker, signed-raw-file **hash**, broadcast acknowledgement, and receipt were rechecked through the pinned original verifier. Earlier C/D records were also verified. File hashes and local evidence paths are in `evidence_manifest.json`.

The original binary RPC responses, signed transaction bytes, keystores, wallet secrets, and attempt journals are **not contained in this ZIP**. They remain in the existing local evidence directories. This digest alone cannot substitute for those original records if a reviewer requests full raw corroboration.

## Scope and limitations

1. The claim and both witness statements are explicitly **synthetic** and do **not** authenticate any external real-world source or prove independent truth.
2. This one live case demonstrates **SS → CORROBORATED**. Live finality for `CONFLICTED`/`UNPROVEN`, revised cases, rejection paths, and concurrency/abuse cases is **not established** by this certificate.
3. Compilation/lint/typecheck, broader regression coverage, provenance of any public repository release, and external reviewer acceptance are **not newly audited** here.
4. This proof applies to Studio Devnet chain 61997 and the exact frozen deployed contract. It is not evidence of production/Mainnet or Bradbury deployment.
5. No new blockchain writes, signing, resimulation, or RPC calls were made by this offline certificate.

## Suggested reviewer conclusion

> One two-witness synthetic positive-path lifecycle is independently hash-reconciled from archived Studio Devnet records: each witness write and the resolution finalized with MAJORITY_AGREE; the contract stores RESOLVED, SS, CORROBORATED, and two exact distinct evidence submissions. Broader scenario and release-readiness certification remain separate tasks.
