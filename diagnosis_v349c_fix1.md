# v3.4.9c final targeted repair: Stage A diagnosis (read-only; no pipeline change made)
Branch fix/v349c-final-quality from build/v349c 87ccedd. Input check: Resume_Pipeline_3_4_9c.zip sha256 2fc1ee8b... equals
the committed release and unpacks to the verified release tree. Data: details/fix1_diagnosis_data.txt, details/fix2_vindexa_trace.txt.

## Fix 1: role-family closings (87/126 = 69%; audit limit 10% = at most 12)
Why the selector rejects specific claims:
1. Single-proof check. The Run 7 wrapper tests only the one proof the v3.4.4 picker returns for a responsibility; another
   on-page proof that does demonstrate it is never tried. Searching all proofs of the page projects: +29 specific.
2. Narrow candidates. Coordinated responsibilities are not split ("implement API endpoints and review pull requests").
3. Literal matching. Plurals ("apis" vs "API"), "front-end" vs "front end", "AI-powered", "proof-of-concept" (GoingOnce
   prototype). Inflection matching alone adds nothing beyond item 1.
4. Genuine lack of evidence (most of the rest). Master evidence has no documentation, API endpoints, unit tests, queries,
   data ingestion, troubleshooting, iOS/mobile, card payments, embedded control, mission software, frameworks/libraries,
   whitepapers. Many candidates are also unusable fragments ("integrate work and life", "develop breakthrough
   technologies", "engineer support a set of checkout APIs", "deliver a substantial project ... what it takes").
5. 16 letters have no candidate at all (already 13 in v3.4.9b, 10.3%, which also failed the audit).

Achievable, measured offline on the release outputs:
| Selector | Specific | Role-family |
|---|---|---|
| Release (Run 7) | 39 | 87 (69.0%) |
| + try every on-page proof (per-item evidence) | 68 | 58 (46.0%) |
| + project-level evidence, inflections, splits, equivalents (upper bound) | 73 | 53 (42.1%) |
The upper bound already includes empty phrases that pass only because every word is generic ("deliver the best results",
"build complex systems", "engineer are expected"); a selector that refuses those lands near 45-50% role-family.
At most 10% is not reachable without inventing responsibilities/evidence or treating keyword overlap as proof.
Per the instructions, Fix 1 stops here. Repetition: 30 of the 31 audit repeat lines are proof-less role-family closings
(the audit then compares the whole closing, company name and "I want" included, with the letter); giving every remaining
role-family closing an on-page proof that supports its claim removes that class, but cannot fix the 10% share.

## Fix 2: vindexa resume (reproduced; root cause found)
v349b fit step: a trimmed page is kept only if the letter is unchanged (v349b_subset_ok). With closing_v349c off (Run 6),
every 3/2/2 attempt changed the closing's proof (the proof follows the page bullets), so attempts were refused until a
later one (Run 6 page: GoingOnce 2, LaunchOps 2). With Run 7 the closing is a proof-less role-family sentence that does
not follow the page, so the first 3/2/2 attempt passes (GoingOnce 3, LaunchOps 1). Trace: details/fix2_vindexa_trace.txt.
Proposed fix (closing_v349c / letters_plain_v349c only; no change to ranking, bullets, Skills, spacing):
- Every page decision sees the Run 6 letter: compose runs with closing_v349c switched off for the letter kept in the plan
  (fit-step comparisons, letter-number check); the grounded closing is chosen afterwards for the output letter only,
  which build_cover_letter writes (the Run 8 swap). Flags off: unchanged paths.
- Expected effect: resumes identical to Run 6 on all 126 built fixtures (vindexa back to 2/2), letters unchanged in rules.

## Decision needed before Stage B
1. Fix 1 target: the 10% line cannot be met with grounded closings. Options: (a) implement the honest improvements
   (try every on-page proof, coordinated splits, a short documented equivalence list, proofs for family closings; about
   46% role-family, audit repeat lines mostly gone) and report the audit as still failing; (b) add verified evidence to
   the master (for example documentation, API endpoints, unit tests) if Jay confirms it, then re-measure; (c) keep Run 7.
2. Fix 2 can proceed independently; one full verification cycle (128 + all gates) covers both once Fix 1 is decided.
