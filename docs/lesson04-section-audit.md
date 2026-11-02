# Lesson 04 section audit

Audited: 2026-11-02 (Asia/Dubai). Original exercise date: 2026-10-28.
Course: https://khanlab.bio/cbio7501-f26/pages/04-git.html
Source revision: `66b2a6a68b8fe9e3c3f6a391a92433e8f37caa8c`.
The current course source was compared with that revision on the audit date
and is unchanged.

This audit describes the original 2026-10-28 execution. A separate
2026-11-02 rerun now preserves real practice commits on
`lesson-04-practice-history`; see `docs/lesson04-practice-run.md`.

## What was actually executed on 2026-10-28

The repository was already initialized and on GitHub before lesson 04.
Existing setup was checked and reused. New Git exercises were executed in a
temporary clone, with real commits, a real merge conflict, and actual
committed deletions followed by restoration. Their commands and output were
captured in `docs/lesson04-checks.txt`. The temporary clone was then removed;
its exercise commits are not reachable from the GitHub main branch.

The final lesson files were published through PR #1 with a squash merge,
following the selected requirement to add only one lesson 04 commit to main.
This means completed exercises and individually published Git commits are
two different claims. Only the former is supported for the temporary exercises.

| Course section | Execution and result | Evidence visible to the instructor |
| --- | --- | --- |
| 1. Is Git set up? | Checked Git 2.56.0 and the existing author identity; did not replace it with the example identity. | Author of the published commits; identity and version recorded in the lesson log. |
| 2. Start tracking the project | Reused the existing repository instead of creating new history; checked ignore rules for raw FASTQ, Pixi environments and results. | Original commit `83393de`; `.gitignore`; `git check-ignore -v` output in the log. |
| 3. The first commit | Reused the original first commit; ran `pixi lock` in the real project and included the lock file in the lesson 04 commit. | `pixi.lock`, `.gitattributes`, commit `c3ade47`. |
| 4. Change, inspect, commit | In the temporary clone, changed README, compared unstaged/staged diffs, unstaged a file without losing it, and separately committed metadata and analysis notes. | Real commands and temporary commit IDs in the log; their final file content is in `c3ade47`. The temporary commit objects were not pushed. |
| 5. Browse the history | Ran `git log --oneline`, `git show --stat HEAD`, and path-specific history in the temporary clone; inspected the main repository history separately. | Command output in the log; public main history remains the three original published commits. |
| 6. Put the project on GitHub | Reused the existing SSH remote; pushed the lesson branch and synchronized main after merging. Did not create another repository or repeat HTTPS authentication. | Public repository, SSH remote, PR #1 and the published commit. |
| 7. Branches | Created `add-decision-log`, committed the decision log, fast-forward merged it and deleted the branch in the temporary clone. | Commands, commit IDs and graph output in the log; no independent public branch/commit objects from that clone. |
| 8. A merge conflict | Created `depth-5` and `depth-10`; triggered a content conflict; resolved it by keeping the proposed comparison of thresholds 2 and 10; verified a two-parent merge commit. | `CONFLICT` output and merge parent IDs in the log; final `docs/decisions.md`. No variant analysis was run. |
| 9. Pull requests and Reproduce check | Created and pushed `lesson-04-readme`; opened and reviewed PR #1; inspected job logs; squash merged; pulled main; deleted merged branch. | Merged PR #1 and green Actions runs. Squash was an intentional adaptation to the single-commit requirement. |
| 10. Tags | Created and pushed the annotated `lesson-04` tag, then checked it points to the final main commit. | Public annotated tag `lesson-04`, pointing to `c3ade47`. |

## Additional exercises and exclusions

- Try it yourself 1: inspected the last change to `docs/decisions.md` and
  its previous version in the temporary clone.
- Try it yourself 2: cloned the local repository into an isolated folder and
  confirmed all seven raw files were absent and verification failed as expected.
  This used a local clone, not a second clone from the GitHub SSH URL. No data
  were downloaded again in this exercise.
- Break it: actually committed deletion of `scripts/download_data.py` and
  `metadata/samples.tsv` in the temporary clone, restored them from `HEAD~1`,
  and verified both files were byte-identical to their earlier versions.
- Optional Going further material was read as reference; not every optional
  undo command (such as stash, amend or revert) was executed.
- Troubleshooting commands were not deliberately run when their associated
  error did not occur.
- Apply it to your own project was outside the selected LTEE-only scope;
  no separate capstone repository was created.
- Lesson 05 analysis tasks and local project-environment installation were
  not performed. The CI task still prints the template placeholder.

## Public evidence checked on 2026-11-02

- Main commit: https://github.com/Haotian-Tang/ltee-project/commit/c3ade47090d2a0b35de4c099405d5888f5d06f96
- Merged PR: https://github.com/Haotian-Tang/ltee-project/pull/1
- Annotated tag: https://github.com/Haotian-Tang/ltee-project/tree/lesson-04
- Main Actions run: https://github.com/Haotian-Tang/ltee-project/actions/runs/40705498577
- Tag Actions run: https://github.com/Haotian-Tang/ltee-project/actions/runs/40705608777

The two Actions runs completed successfully. They checked installation of
locked dependencies and execution of the placeholder, not a completed
variant-calling pipeline.

## History policy for future records

Every substantive action should be recorded with its lesson and section,
the command/change, its result, and the corresponding real commit or PR.
Text transcripts should be labelled as transcripts. If an exercise is
repeated later to publish its actual commits, it must use the real new date
and be labelled as a repeat; earlier history and timestamps must not be rewritten.

## Published 2026-11-02 repeat

The missing independently inspectable practice commits have now been
supplemented through a new, explicitly dated rerun on
`lesson-04-practice-history`. See `docs/lesson04-practice-run.md` for
the full section map, actual commit links, merged PR #2 and checks.
The original main history and lesson-04 tag were retained.
