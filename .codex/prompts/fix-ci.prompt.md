You are fixing a failing CI run in this repository.

Requirements:
1. Only change production code under `src/` unless absolutely necessary.
2. Never weaken, skip, delete, or rewrite tests to make them pass.
3. Keep changes minimal and focused on the test failures.
4. Preserve existing public function names and behavior unless tests require a bug fix.
5. Do not modify files under `tests/`, `.github/workflows/`, or `.codex/prompts/`.
6. After edits, run tests and ensure all tests pass.

Input available in the workspace:
- Python source code in `src/`
- tests in `tests/`
- failing test output in `pytest.log`

Task:
- Read `pytest.log` to identify failures.
- Apply a minimal patch that fixes the root cause.
- Re-run tests and confirm they are green.
- Summarize what changed in a short commit message.
