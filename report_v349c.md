# v3.4.9c release (Run 9) - Resume_Pipeline_3_4_9c.zip, from Resume_Pipeline_3_4_9c_8.zip and Resume_Pipeline_3_4_9b.zip
PIPELINE_VERSION "v3.4.9c" ("v3.4.9b" when all nine v3.4.9c flags are off). 47 flags; the nine v3.4.9c flags default true.
Hash lock: pipeline b04aa71d | master 019e5b87 | bank 914805e9 | template a3aaddd9 | context md b43948bf (instructions
7,574 characters). Sources changed vs v3.4.9b: pipeline, master.json, template, context md (bank, bank_check, plan_template
unchanged). The ZIP's folder is Resume_Pipeline_3_4_9c (as each release names it); no file inside was renamed.
Details: details/run9_full128.txt, details/run9_gate16.txt.

## Gates
| Gate | Result |
|---|---|
| 128 fixtures, flags on, exit 0 | 128/128; 126 PASS + 2 expected stops (fonzi, cisco_no_title) |
| One US Letter page, >= 10.5pt spare | 126/126, 10.51-10.77pt unrounded |
| All nine flags off vs original v3.4.9b (GATE16) | 16/16 byte-identical; template rebuilds to dc281778 |
| Flags on: GATE16 vs the same fixtures in the 128 run | 16/16 identical (determinism) |
| Selftests v341-v349b (14) | all pass; selftest_v348b 80/80 (the 3 hash-lock failures resolved) |
| bank_check / golden_check / score_all | 120 variants 0 failing / 12/12 / resume 9.96, letter 9.98 |
| Grep: resumes + letters | no "Expected", "1st Place", "Copart", "Cloud Practitioner", Agentic AI coursework |
| Grep: letters | no tool names, no we/our/us, no digits outside the graduation sentence (and the posting's own title) |
| audit_v344 (unchanged) | exit 1: role-family closings 69.0% > 10%; 31 repeat lines (30 proof-less family closings) |

## Found in Run 9 and fixed (letters_plain_v349c / must_framework_v349c; all 128 rerun after the fixes)
- laminar "Jr. ... role" opening cut at "Jr." (exit 2); twitch 118 words; "Another project is fraud detection models".
- Hooks: tool words as adjectives/objects made hooks fall back to cut phrases ("build features end") or a generic line;
  now de-tooled and checked with the pipeline's own posting tests. Swift (ios_randstad) and other industry tools now count.
- 15 AI-coding postings had lost that evidence (no "Claude Code"): now "An AI coding assistant helped me write RIPPLE ...".
- report.json ranking_v349.rank was stale after a must promotion, so golden_check read ebsco_sde1 rank1 wrong (now 12/12).
- Older selftests and score_all expected v3.4.9b pages / flag counts; updated where necessary (listed in CHANGES.md).

## Open findings (not changed; for Jay)
- Run 7 grounding sends 87/126 closings to the role-family closing (v3.4.9b: 13). That is the approved rule; it is why
  audit_v344 fails. A looser support check (synonyms, partial support) would restore specific closings.
- vindexa's resume differs from Run 6 (GoingOnce 3 / LaunchOps 1 bullets instead of 2 / 2): its fit step keeps a trimmed
  page only when the letter is unchanged, and Run 7 changed its closing. Run 7's resume gate held on GATE16 only.

## Deviations (documented in NOTES_v3_4_9c.md and the context md section 0-v349c)
0.3in side margins and Standard spacing on every page (approved; not an exact Trial2 match); cardinal Skills exception
(approved); Run 5 spacing grows only while 10.5pt spare remains; letters allow digits in the posting's own title.
Migration: paste the new instructions, re-upload the 7 Sources (4 changed), expect hash PASS as above.
