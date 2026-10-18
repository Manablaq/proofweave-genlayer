# Reviewer notes and known limitations

## What is proven

One synthetic on-chain claim lifecycle with two distinct witnesses and one resolution on **Studio Devnet, chain 61997**. Each of the three write transactions finalized with `MAJORITY_AGREE`. Final contract reads independently confirmed both evidence slots and `RESOLVED / SS / CORROBORATED`.

## What is not claimed

- Real-world verification: synthetic witness statements are not authenticated external records.
- Live alternative outcomes: `CONFLICTED` and `UNPROVEN` are code paths, but not finalized live examples in this submission.
- External release audit: the certificate did not newly audit general repository documentation, CI, typechecking, or production readiness.
- A frontend, user-facing dApp, or production deployment: this project is a **standalone Intelligent Contract**.

## Source and audit trail

The exact deployed contract source is `contracts/proof_weave.py` SHA-256 `a57384aeb9140eda87f8b593adc697343370ae504ca6f37d30c54cefded50d7f`.

The included sanitized certificate is a **read-only digest**. Private archive response bytes, wallet files, and signed transaction bytes are not published. The certificate reports `REVIEWER_ACCEPTANCE=NOT_CLAIMED` and correctly separates finality from a reviewer judgment.

## Reviewer checks

Read `docs/LIVE_VERIFICATION.md`; verify the three hashes and contract views; check the archived manifest. Confirm that this submission meets the review criteria for one finished positive-path demonstration, without conflating it with broader scenario certification.
