# v3.4.9c fix1: UNVERIFIED handoff (paused on request)
Package: Resume_Pipeline_3_4_9c_fix1_UNVERIFIED.zip (pipeline b209a287; all Sources, 3_validation tests and the 128 fixture
JDs; UNVERIFIED.txt inside). Built from the verified release (build/v349c 87ccedd, Resume_Pipeline_3_4_9c.zip), which is
unchanged, like every earlier checkpoint. Code change = release + details/patch_v349c_fix1.py (pipeline only); the
instructions hash lock and 0_SETUP_STEPS expected hash were updated for the new pipeline hash. Not production-ready.

## Fix 2: resume/letter isolation (targeted tests passed; full 128 NOT run)
Change: compose_bank_cover_letter composes the letter kept in the plan with closing_v349c switched off (the run 6
letter), so the fit step's letter comparison and the letter-number check see exactly what Run 6 saw; the grounded closing
is chosen afterwards for the written letter only (plain letters; with letters_plain_v349c off the run 7 letter is composed
a second time and the plan is restored). build_cover_letter writes the written letter; v349b_note_letter and
_v33_quality read the run 6 letter.
Targeted results (details/fix1_targeted_tests.txt), all exit 0:
- vindexa: GoingOnce 2 / LaunchOps 2 with closing_v349c on, off, and with letters_plain_v349c off; resume byte-identical
  to the verified Run 6 output (the release had 3 / 1).
- vindexa, ebsco_sde1, figure, cardinal, alml_engineer, macys: resume byte-identical across closing on / closing off /
  plain off and equal to Run 6, while every closing text changed.
- 12-fixture run (all flags on): resume .tex, tracker rows and outreach identical to Run 6 on 12/12; plain-letter gate 12/12.
Not yet shown: the other 116 fixtures, flag-off identity against v3.4.9b, determinism.

## Fix 1: grounded specific closings (UNFINISHED; stopped on request)
Done: v349c_grounded_closing tries every posting responsibility (and each half of "X and <verb> Y") against every
on-page proof; refuses vague fragments (v349c_meaningful); no proof-kind shortcut (each specific word must be in the
cited proof's own evidence); plural / front-end / back-end / full-stack spellings; compounds need the whole term
("low-level" only matches Pintos); plain letters check repetition against the written letter; role-family closings get
an on-page proof that shows their claim (or the general claim) when one exists.
Measured on the 12-fixture sample only: 3 specific / 9 role-family (75%; audit_v344 still FAIL, 10% unchanged).
Unresolved:
1. False positive found: elevenlabs "build internal platforms or services used by other engineering teams" passes because
   the inherited 5-letter stem match lets "internal" match "interviewed" and "engineering" match the job title, and the
   Experience evidence text includes anchor notes ("not used on the resume"). The stem rule and the Experience corpus need
   tightening before any count is trusted; doordash_mdx "build agentic developer support" (agentic <- "AI agents") needs review.
2. Strict matching lowers the specific count below the Stage A estimate (46% was measured with looser per-item matching);
   the achievable share must be re-measured on all 128 after item 1.
3. Repetition: on the sample 1 audit repeat line (l3harris, proof-less family closing; the audit counts the "3" in
   "L3Harris" as a number).
4. Fix 1 changes letters only; under Fix 2 it cannot change resumes, but that is only shown on the tested fixtures.

## Running the full verification independently
Unzip Resume_Pipeline_3_4_9c_fix1_UNVERIFIED.zip; in Resume_Pipeline_3_4_9c_fix1_UNVERIFIED/3_validation/:
1. 128 fixtures, flags on: `OUT=out_fix1 python3 run_all.py` (or `BATCH=k/48` for k = 1..48 in a time-limited shell);
   every fixture must exit 0 (fonzi, cisco_no_title are the expected stops).
2. Resumes vs the release: compare each out_fix1/<fixture>/out/<Key>.tex, tracker_row.json and outreach.json with a
   run of the release ZIP (Resume_Pipeline_3_4_9c.zip); expected identical except vindexa, which must equal Run 6
   (GoingOnce 2 / LaunchOps 2).
3. Flag-off identity: `V347_FLAGS_OFF=data_v349c,page_v349c,thesis_v349c,coursework_v349c,layout_v349c,spacing_v349c,must_framework_v349c,closing_v349c,letters_plain_v349c OUT=out_off python3 run_all.py`
   on the GATE16 fixtures; compare with the original Resume_Pipeline_3_4_9b.zip outputs (timing keys ignored).
4. `python3 selftest_v341.py` ... `selftest_v349b.py` (14 files); bank_check (0_SETUP_STEPS step 6);
   `python3 golden_check.py out_fix1 fix1` (expect 12/12); `python3 audit_v344.py out_fix1` (role-family share and
   repeat lines); `python3 score_all.py out_fix1`; run step 1 twice on GATE16 for determinism.
