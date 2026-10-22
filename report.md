# Run 1 (data) - Resume_Pipeline_3_4_9c_1.zip, from Resume_Pipeline_3_4_9b.zip (input unchanged)
Flag `data_v349c` (v347_flags, default true, 39 flags). PIPELINE_VERSION left at v3.4.9b so flag-off reports stay byte-identical.
- Coursework = the 9 courses you listed (master); "Agentic AI" removed as coursework (rule text, education_v345 text); kept as a skill.
- Education date "August 2025 -- December 2026" in template, master, `_v348b_post_run` (also fails on any "Expected"), selftests v348b/v349b, diff_gate/predict v348b (+ predicted_changes_v348b.json patterns).
- Letter bank: removed "We won 1st place." (cover_letter_bank.letter_sentences.projects.goingonce). Kept: "On a four-person hackathon team..." and closing_proofs goingonce.negotiate (evidence wording, no award claim); the resume Awards line is not letter bank.
- Hashes: template afe49385, master b67da266 (master.source.template_sha256 updated), bank 914805e9 unchanged; pipeline pins updated. Only 8 files differ from the input ZIP.
## GATE16 (baseline = unmodified ZIP; 16/16 PASS in baseline, flag on and flag off)
- Flag off: 16/16 byte-identical to baseline (every output file; only report timestamps/durations ignored). Re-checked from the committed ZIP on ebsco_sde1, allergan, macys: flag off = baseline, flag on = earlier flag-on run.
- Letters changed: 0/16. Tracker rows, outreach: 0/16 changed. Resume .tex: 15/16 differ only in the Education date line.
- GATE NOT MET, ebsco_sde1 (conflict, not fixed): its "Relevant coursework" line is dropped. Measured on the same page: shipped 3-course line 12.0pt spare; no line 23.7pt; nine courses (208 chars, wraps to 2 lines) 0.3pt. Required spare is 10pt (V33_MIN_BUFFER_PT), so the line cannot stay by 9.7pt. Keeping it needs a smaller buffer, spacing or font, or one fewer bullet; each weakens the gate or changes more than the date, so none was done.
- report.json only: skills_text_hash 16/16 (template hash is its key); macys, nvidia_infra ats_coverage "Algorithms" gets also_in "education" (new course name is in the scanned education text). judge_packet.md, quality_v33.json, tex_sha256.txt follow the resume.
- No "Expected" and no Agentic AI coursework in any flag-on output, template, master or bank (flag-off restore constants and old-version comments in the pipeline keep the old strings).
## Checks
- bank_check: 120 variants, 0 failing. selftest_v349b: ALL PASS (43). selftest_v348b: 77 pass, 3 FAIL (unresolved, deferred to Run 9, not passed).
- The 3 failures are "hash lock lists" resume_pipeline_v3_2.py, master.json, Resume_Template_CURRENT.tex. They read the lock in 2_PROJECT_INSTRUCTIONS_paste.txt, which is byte-identical to the input's and still holds 76c1c6ea / d4e92491 / 137af61b; new values: pipeline 2038c822, master b67da266, template afe49385. Bank and md entries pass.
- Selftest edits: flag count 39; data_v349c added to the flag-off lists that compare with older baselines; the md "Dates:" check in selftest_v348b still expects "Expected" (md is a doc).
- Not run (as instructed): all 128 fixtures, selftests v341-v349a, diff_gate on full baselines.
## Deferred to Run 9
Docs still say "Expected" / Agentic AI coursework: Master_Resume_Context md (lines 38, 39, 83, 245, 252, 256, 515), CHANGES/NOTES/DIFF files, and the instructions hash lock above.
