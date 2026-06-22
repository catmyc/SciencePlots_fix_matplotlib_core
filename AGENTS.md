# Repository Guidelines

## Project Structure & Module Organization

SciencePlots is a `src`-layout Python package. Runtime code lives in
`src/scienceplots/`; `__init__.py` registers bundled styles with Matplotlib, and
`styles_discovery.py` recursively loads style directories. Style sheets are
under `src/scienceplots/styles/`, grouped into `color/`, `journals/`,
`languages/`, and `misc/`. Tests and fixtures are in
`src/scienceplots/tests/`. The gallery generator is
`examples/plot-examples.py`, with reference images in `examples/figures/`.
Packaging metadata is defined in `pyproject.toml` and `MANIFEST.in`.

## Matplotlib Compatibility Focus

This fork removes reliance on Matplotlib's deprecated internal style API.
Do not access `plt.style.core` or import `matplotlib.style.core`; Matplotlib 3.11
stopped exposing the former and deprecated the latter. Preserve recursive
style discovery through public APIs, import-time registration, and
synchronization of `plt.style.library` and `plt.style.available`. Update
`test_matplotlib_required_api_existence` when the required public API surface
changes, and test against the oldest and newest supported Matplotlib versions.

## Build, Test, and Development Commands

- `python -m pip install -e '.[test]'` installs the package and test dependencies
  in editable mode.
- `pytest` runs the configured test suite.
- `pytest src/scienceplots/tests/test_scienceplots.py -v` runs the core
  registration and rendering checks.
- `ruff check .` applies the same lint check used by CI.
- `python examples/plot-examples.py` regenerates gallery images; it requires
  LaTeX and relevant language fonts for all styles.

## Coding Style & Naming Conventions

Use four-space indentation and an 88-character line limit. Follow Ruff rules
from `pyproject.toml`; type annotations are optional. Use `snake_case` for
functions, fixtures, and modules, and `test_<behavior>` for tests. Name style
files by their public style identifier, such as `no-latex.mplstyle` or
`discrete-rainbow-15.mplstyle`.

## Testing Guidelines

Use pytest and keep tests deterministic and backend-independent. New styles
must be discoverable, present in Matplotlib's style library, and render a
figure successfully. Compatibility fixes should include a focused regression
test reproducing the affected Matplotlib API behavior. CI covers Python
3.10–3.14 and installs LaTeX plus Noto CJK fonts.

## Commit & Pull Request Guidelines

Use concise, imperative commit subjects, optionally with a scope such as
`[CI]`; reference issues or PRs when relevant. Discuss new styles or behavioral
changes in an issue first. Pull requests should explain the compatibility
problem, list tested Python and Matplotlib versions, and report `pytest` and
Ruff results. Include before/after figures for visible style changes.
