# Testing and verification report

| Area | Established result | Evidence / boundary |
|---|---|---|
| Contract Direct Mode regression | 14/14 passed, 0 RuntimeWarnings | Original strict test log hash-verified locally during reviewer certification; original log is not in sanitized evidence ZIP |
| Witness C on Studio Devnet | `FINALIZED`, `MAJORITY_AGREE` | Live transaction hash in `LIVE_VERIFICATION.md` |
| Witness D on Studio Devnet | `FINALIZED`, `MAJORITY_AGREE` | Live transaction hash in `LIVE_VERIFICATION.md` |
| Resolution on Studio Devnet | `FINALIZED`, `MAJORITY_AGREE`; `RESOLVED`, `SS`, `CORROBORATED` | Live contract views and preserved finality response hashes |
| Reviewer certificate | PASS | Offline certified against 11 SHA-pinned finality responses |
| Sanitized reviewer ZIP | PASS | Four files, 27 references; ZIP SHA-256 `1dd66e4e0b20529b29d8ea1bf1cf909de674942414299f6e64fd4132d583e8cd` |
| Deployed contract source | SHA-256 verified | `a57384aeb9140eda87f8b593adc697343370ae504ca6f37d30c54cefded50d7f` |

**Not established by this report:** production/Bradbury deployment, new compilation/lint/typecheck, source-revision release CI, independent third-party source authenticity, live `CONFLICTED` or `UNPROVEN` outcomes, concurrency/abuse or revision-path live coverage, external reviewer acceptance. No additional blockchain write is warranted for this report.

Test files copied into `tests/` by the local release builder are a snapshot of local Python test sources, **not** a claim those exact published files were independently rerun after release creation. Reviewers should run them in the appropriate pinned GenLayer Direct Mode environment.
