# Run 1 (data) - Resume_Pipeline_3_4_9c_1.zip, from Resume_Pipeline_3_4_9b.zip (input unchanged)
Flag `data_v349c` (v347_flags, default true, 39 flags). PIPELINE_VERSION left at v3.4.9b so flag-off reports stay byte-identical.
- Coursework = the 9 courses you listed (master); "Agentic AI" removed as coursework (rule text, education_v345 text); kept as a skill.
- Education date "August 2025 -- December 2026" in template, master, `_v348b_post_run` (also fails on any "Expected"), selftests v348b/v349b, diff_gate/predict v348b (+ predicted_changes_v348b.json patterns).
- Letter bank: removed "We won 1st place." (cover_letter_bank.letter_sentences.projects.goingonce). Kept: "On a four-person hackathon team..." and closing_proofs goingonce.negotiate (evidence wording, no award claim); the resume Awards line is not letter bank.
- Hashes: template afe49385, master b67da266 (master.source.template_sha256 updated), bank 914805e9 unchanged; pipeline pins updated. Only 8 files differ from the input ZIP.
## GATE16 (baseline = unmodified ZIP; 16/16 PASS in baseline, flag on and flag off)
- Flag off: 16/16 byte-identical to baseline (every output file; only report timestamps/durations ignored).
- Letters changed: 0/16 (no GATE16 letter uses the GoingOnce sentence). Tracker rows, outreach: 0/16 changed.
- Resume .tex: 15/16 differ only in the Education date line.
- Resume DEVIATION (gate not met): ebsco_sde1 also loses its "Relevant coursework" line. The posting asks for coursework; the 9-course list wraps to 2 lines, the page then has under 10pt spare, so the existing fit step drops the line (logged in report.json).
- report.json only: skills_text_hash (template hash is its key) 16/16; macys, nvidia_infra ats_coverage Algorithms gets also_in "education" (new course "Algorithms Analysis & Design" is in the education text the checker scans). judge_packet.md, quality_v33.json, tex_sha256.txt follow the resume.
- No "Expected" and no Agentic AI coursework in any flag-on output, template, master or bank. Left on purpose: flag-off restore constants and old-version comments in the pipeline.
## Checks
- bank_check: 120 variants, 0 failing. selftest_v349b: ALL PASS (43). selftest_v348b: 77 pass, 3 fail: "hash lock lists" pipeline, master, template - they read the hash lock in 2_PROJECT_INSTRUCTIONS_paste.txt, which stays unedited until the final run.
- Selftest edits: flag count 39; data_v349c added to the flag-off lists that compare with older baselines; the md "Dates:" check in selftest_v348b still expects "Expected" because the md is a doc.
- Not run (as instructed): all 128 fixtures, selftests v341-v349a, diff_gate on full baselines.
## Open for the final run
Docs still say "Expected" / Agentic AI coursework: Master_Resume_Context md (lines 38, 39, 83, 245, 252, 256, 515), CHANGES/NOTES/DIFF files, 2_PROJECT_INSTRUCTIONS hash lock (pipeline, master, template).
