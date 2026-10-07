# Step 1: Give each part a home

Use this small structure. Keep all application code inside `calculator/` so coverage measures the whole application.

```
calculator/
    __init__.py
    __main__.py
    operations.py
    calculation.py
    commands.py
    cli.py
tests/
requirements.txt
README.md
.github/workflows/tests.yml
```

Use Python 3.12 or newer. Create a virtual environment and put these test tools in `requirements.txt`:

```
pytest>=8,<10
pytest-cov>=7,<8
```

```
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows PowerShell instead:
# .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Add `.venv/`, `__pycache__/`, `.pytest_cache/`, `.coverage`, and `htmlcov/` to `.gitignore`. Commit your source and tests, not your virtual environment.
The starter already contains addition, the calculation classes, a few example tests, and the workflow. You must add the remaining operations, commands, CLI, and tests. A green starter check does **not** mean the assignment is complete.

---

[Back to the contents](../README.md) · [Start with forking](00-fork-and-submit.md)

Next: [Step 2: Make operations with static methods](03-step-2-make-operations-with-static-methods.md)
