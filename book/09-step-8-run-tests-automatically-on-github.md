# Step 8: Run tests automatically on GitHub

Create `.github/workflows/tests.yml` and copy this workflow. Each push and pull request runs your tests on a fresh computer. A green check means the test command passed.

```
name: Calculator tests

on: [push, pull_request]

permissions:
  contents: read

jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v7
        with:
          python-version: '3.12'
      - name: Install test tools
        run: python -m pip install -r requirements.txt
      - name: Run tests and require 100% coverage
        run: python -m pytest --cov=calculator --cov-report=term-missing --cov-fail-under=100
```

Commit and push the workflow, source, tests, and requirements. Open your repository's **Actions** tab, select **Calculator tests**, and confirm that the latest run passes with 100% coverage. If it fails, open the failed step, fix the problem, and push again. The workflow file must be present; a screenshot alone does not replace it.
---

[Back to the contents](../README.md) · [Start with forking](00-fork-and-submit.md)

Next: [Step 9: Explain your design in the README](10-step-9-explain-your-design-in-the-readme.md)
