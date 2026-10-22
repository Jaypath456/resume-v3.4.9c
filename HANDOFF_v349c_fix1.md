# v3.4.9c fix1 handoff (step 2: closing evidence matching) - UNVERIFIED
Status: UNVERIFIED until the independent full 128-fixture verification passes. Not production-ready.
Branch fix/v349c-final-quality; base commit cd52a58 (first handoff); this handoff is the next commit on the branch.
Release untouched: build/v349c 87ccedd, Resume_Pipeline_3_4_9c.zip (sha256 2fc1ee8b...), Resume_Pipeline_3_4_9b.zip.

## Outer archive v349c_fix1_handoff_UNVERIFIED.zip
1. Resume_Pipeline_3_4_9c_fix1_UNVERIFIED.zip - updated build: pipeline 8f0a1df7 (release + details/patch_v349c_fix1.py +
   details/patch_v349c_fix1_step2.py), all Sources, 3_validation tests and the 128 fixture JDs; UNVERIFIED.txt inside.
   Hash lock (instructions) and 0_SETUP_STEPS expected hash updated for the pipeline; master 019e5b87, bank 914805e9,
   template a3aaddd9, context md b43948bf unchanged. No internal file renamed.
2. Resume_Pipeline_3_4_9c.zip - the verified release, unchanged (byte-identical to build/v349c).
3. Resume_Pipeline_3_4_9b.zip - the original baseline, unchanged.
4. HANDOFF_v349c_fix1.md - this report.

## What changed in step 2 (Fix 1 evidence matching only)
- Cited evidence = the proof sentence; for a project proof its evidence item's text and claim atoms; for an Experience
  proof only the bullets that proof names. Removed from the evidence: job titles, employer names, evidence-anchor notes,
  project tags and keyword labels ("full-stack/backend", "system design", terms lists).
- Whole-word matching on base forms (plural, -ing, -ed, final -e): "internal" no longer matches "interviewed"; "APIs" =
  "API". Compounds need the whole term or every specific part of 4+ letters. No proof-kind shortcut.
- "dependable" joins the role-family quality words (same list for the selector and the claim check, like "careful").
- Fix 2 (resume/letter isolation) unchanged.

## Targeted test results (details/fix1_step2_targeted_tests.txt)
Fixtures: the 12-fixture sample (vindexa, alml_engineer, doordash_mdx, elevenlabs, zoro_fullstack, audit01, l3harris,
arclight, corvex, fidelity, harvey, macys) + doordash; closing_v349c off for vindexa, elevenlabs, doordash_mdx.
- Exit codes: 16/16 = 0.
- Questionable closings removed: elevenlabs ("internal platforms ... engineering teams": internal/engineering not in the
  cited bullets) and doordash_mdx ("agentic developer support": not in RIPPLE's cited evidence) now take honest
  role-family closings with an on-page proof that shows the claim (both: "build dependable, well-tested software ...").
- Closings in the sample: 0 specific / 13 role-family (100%). The sample was drawn from closings that were role-family in
  the release, so it does not measure the full share.
- Independent grounding check (own evidence assembly from master.json): no specific closing in the sample to check (0/0).
- Plain-letter rules + resume, tracker and outreach identical to Run 6: 13/13.
- Resume isolation: resume .tex identical with closing_v349c on and off (vindexa, elevenlabs, doordash_mdx).
- vindexa: GoingOnce 2 / LaunchOps 2 (flags on, closing off, and Run 6).
- audit_v344 on the sample only: 0 repeat lines; role-family 100% (> 10%: FAIL).

## Unresolved issues
1. The full-128 role-family share is unknown and expected to be HIGHER than the release's 69%: with strict cited
   evidence many of the release's 39 specific closings (which relied on 5-letter stems, tags and the proof-kind
   shortcut) are likely to fall back. audit_v344's 10% line will FAIL; the threshold was not changed.
2. Master evidence is the limit: most posting responsibilities name things no cited evidence item states (API
   endpoints, documentation, unit tests, infrastructure, iOS, ...). More specific closings need verified evidence added
   to master.json by Jay, not looser matching.
3. Not run on this code: full 128, 14 selftests, bank_check, golden_check, full audit, flag-off identity, determinism.

## Verification commands (inside the unzipped Resume_Pipeline_3_4_9c_fix1_UNVERIFIED/3_validation/)
1. `OUT=out_fix1 python3 run_all.py` (or `BATCH=k/48 OUT=out_fix1 python3 run_all.py`, k = 1..48); every fixture exits 0;
   fonzi and cisco_no_title are the expected stops.
2. Run the release the same way (`OUT=out_rel`, from Resume_Pipeline_3_4_9c.zip); every <Key>.tex, tracker_row.json and
   outreach.json must be identical except vindexa, which must show GoingOnce 2 / LaunchOps 2 (as Run 6).
3. Flag-off identity: `V347_FLAGS_OFF=data_v349c,page_v349c,thesis_v349c,coursework_v349c,layout_v349c,spacing_v349c,must_framework_v349c,closing_v349c,letters_plain_v349c OUT=out_off python3 run_all.py`
   and compare with the same run of Resume_Pipeline_3_4_9b.zip (timing keys ignored; GATE16 is enough).
4. `for t in selftest_v3*.py; do python3 $t; done` (14 files); bank_check per 0_SETUP_STEPS step 6;
   `python3 golden_check.py out_fix1 fix1` (expect 12/12); `python3 audit_v344.py out_fix1` (report the role-family share
   and repeat lines as measured); `python3 score_all.py out_fix1`; repeat step 1 on GATE16 for determinism.
