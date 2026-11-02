# Recorded lesson 04 rerun

Executed on 2026-11-02 (Asia/Dubai), using real current commit dates.
This is an explicitly labelled repeat, not a recreation of earlier timestamps.

Branch: `lesson-04-practice-history`.
Original main: `c3ade47090d2a0b35de4c099405d5888f5d06f96` (unchanged).
Original `lesson-04` annotated tag object: `60904d5506584bf4bde157aeba4cb5e289364644` (unchanged).
Rerun baseline: lesson 03 commit `b97a2a7c143dd0c2f818325aecd9789d36ed97a0`.

## Section-by-section evidence

| Section | Actual action and result | Inspectable evidence |
| --- | --- | --- |
| 1 | Read Git version and existing author identity; reused the valid setup. | [Setup-check commit](https://github.com/Haotian-Tang/ltee-project/commit/fa4eed29d7448c56e9d03b82c36688e2a3ff8c4d) |
| 2 | Checked repository status, remote and ignore rules; reused initialization. | [Setup-check commit](https://github.com/Haotian-Tang/ltee-project/commit/fa4eed29d7448c56e9d03b82c36688e2a3ff8c4d) and full transcript |
| 3 | Reused the exact published lock versions, ran `pixi lock`, verified no version or byte changes, and committed the lock file. No local environment installation. | [Lock-file commit](https://github.com/Haotian-Tang/ltee-project/commit/17e7709074ba7b4413068621933d2ebb7ba0ca75) |
| 4 | Changed README, inspected working/staged diffs, separately committed metadata and notes, and verified unstaging keeps the working file. | Three separate section 4 commits below |
| 5 | Used full and path-specific `git log` and `git show` to inspect history. | [Inspection record](https://github.com/Haotian-Tang/ltee-project/commit/20e4683b0c1b797814400c35c65442ea626e279f) |
| 6 | Pushed the actual practice branch through the existing GitHub SSH remote. | Public branch history and successful push in the transcript |
| 7 | Created a decision-log branch, committed, fast-forward merged and deleted its label. | [Decision-log commit](https://github.com/Haotian-Tang/ltee-project/commit/20b57bcc9f4edd8c583b432a9f25fdde812e85f9) |
| 8 | Made two real proposal commits, triggered `CONFLICT (content)`, and resolved it with a verified two-parent merge. | [Conflict-resolution merge](https://github.com/Haotian-Tang/ltee-project/commit/96df606ab363927388dbc50d75ed27ce6c036fe7) |
| 9 | Pushed a README/CI branch, reviewed PR #2 and its job log, waited for green Actions, performed a normal merge and cleaned up its branch. | [Merged PR #2](https://github.com/Haotian-Tang/ltee-project/pull/2), [green check](https://github.com/Haotian-Tang/ltee-project/actions/runs/41438086811) |
| 10 | Verified and retained original `lesson-04`; the final repeated exercise state is marked by a separate annotated `lesson-04-practice-2026-11-02` tag. | Both GitHub tags, with the original unchanged |

## Real commits retained in this branch

| Step | Commit | What changed |
| --- | --- | --- |
| 1-2 | [`fa4eed2`](https://github.com/Haotian-Tang/ltee-project/commit/fa4eed29d7448c56e9d03b82c36688e2a3ff8c4d) | Lesson 04 sections 1-2: record Git setup checks |
| 3 | [`17e7709`](https://github.com/Haotian-Tang/ltee-project/commit/17e7709074ba7b4413068621933d2ebb7ba0ca75) | Lesson 04 section 3: commit the lock file |
| 4a | [`c30d0b1`](https://github.com/Haotian-Tang/ltee-project/commit/c30d0b12486db57bab044d0a95b51afc2a241071) | Lesson 04 section 4: explain the project purpose |
| 4b | [`9e3efc9`](https://github.com/Haotian-Tang/ltee-project/commit/9e3efc9da11dc5bcaba19a38374a5b40f4e839fd) | Lesson 04 section 4: document read preprocessing |
| 4c | [`37b028f`](https://github.com/Haotian-Tang/ltee-project/commit/37b028fb22bf856a970a031a5d80a075d247fdeb) | Lesson 04 section 4: start analysis notes |
| 5 | [`20e4683`](https://github.com/Haotian-Tang/ltee-project/commit/20e4683b0c1b797814400c35c65442ea626e279f) | Lesson 04 section 5: record history inspection |
| 7 | [`20b57bc`](https://github.com/Haotian-Tang/ltee-project/commit/20b57bcc9f4edd8c583b432a9f25fdde812e85f9) | Lesson 04 section 7: start a decision-log branch |
| 8a | [`a61c863`](https://github.com/Haotian-Tang/ltee-project/commit/a61c863956a8c2eae1cd0e76611b08717efde283) | Lesson 04 section 8: propose minimum depth 5 |
| 8b | [`679fe8c`](https://github.com/Haotian-Tang/ltee-project/commit/679fe8c6aebc8867c2311e1afb513c09f1272a46) | Lesson 04 section 8: propose minimum depth 10 |
| 8c | [`96df606`](https://github.com/Haotian-Tang/ltee-project/commit/96df606ab363927388dbc50d75ed27ce6c036fe7) | Lesson 04 section 8: resolve the depth conflict |
| 9 | [`d92d0b7`](https://github.com/Haotian-Tang/ltee-project/commit/d92d0b7eef35ddde77c8b9673db608c747747fa1) | Lesson 04 section 9: document data access and CI |
| 9 merge | [`cb3b8a5`](https://github.com/Haotian-Tang/ltee-project/commit/cb3b8a56d1da0a0c1704aa55214450814b3a3e52) | Lesson 04 section 9: merge the practice pull request |
| Break it: delete | [`42e8b0f`](https://github.com/Haotian-Tang/ltee-project/commit/42e8b0fa8f2d241f000b154363ba1a1015b87672) | Lesson 04 break-it: commit a practice deletion |
| Break it: restore | [`dff69e0`](https://github.com/Haotian-Tang/ltee-project/commit/dff69e00cb9fe2b453991cb52cd3a6ad7b0ef7e9) | Lesson 04 break-it: restore the deleted files |

## Additional exercises

- Inspected the last decision-log change and its earlier version with path history and `git show HEAD~1:docs/decisions.md`.
- Actually cloned the published practice branch from GitHub over SSH. Only README.md was present in data/raw; verification correctly reported all seven raw files missing. No data were downloaded.
- Actually committed deletion of the download script and sample sheet, then restored and committed both files. SHA-256 comparisons proved exact restoration.
- The optional undo reference, failure-specific troubleshooting and separate capstone project are not claimed as executed. They are not needed for the selected LTEE Git exercises.

## Full command record

See `docs/lesson04-practice-transcript.txt` for timestamps, commands, output and exit codes. The transcript is evidence of actual execution; the links above identify the corresponding real Git objects.
The final documentation commit records this map and transcript; its own hash is available in the branch history.

Only lesson 04 was repeated. pixi.toml and the placeholder reproduce task are unchanged. No analysis pipeline or local project environment was installed.
The original 2026-10-28 audit is in `docs/lesson04-section-audit.md` and is kept distinct from this new execution.
