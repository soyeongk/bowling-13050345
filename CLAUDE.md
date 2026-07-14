# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project status

This repository currently contains only project scaffolding (PyCharm `.idea/` config and a `.venv/` virtual environment for Python 3.14) — no source code, tests, or dependency manifest exist yet. This is a TDD kata starting from a blank slate, so there is no existing architecture to preserve; follow the requirements below when creating the initial structure.

## Environment

- Python 3.14 (CPython), virtual environment at `.venv/`.
- Only `pip` is currently installed in the venv — no test framework (e.g. pytest) has been added yet. Install one as part of setting up the kata (e.g. `.venv\Scripts\pip install pytest`) and record it in a `requirements.txt` or `pyproject.toml`.
- Activate the venv on Windows: `.venv\Scripts\activate`.
- Once a test framework is in place, run the suite with the equivalent of `.venv\Scripts\pytest` and a single test via `.venv\Scripts\pytest path/to/test_file.py::test_name`.

## Kata: The Bowling Game

Implement a `Game` class with two methods:

- `roll(pins: int) -> None` — called once per ball thrown; `pins` is the number of pins knocked down.
- `score() -> int` — returns the total score for the game.

Do not implement input validation for illegal rolls/frame counts, and do not expose mid-game/per-frame scores — the kata scope is the scoring algorithm only.

### Scoring rules

- A game has 10 frames; each frame is normally 2 rolls to knock down 10 pins.
- **Spare** (10 pins across 2 rolls): frame score = 10 + pins knocked down on the *next 1 roll*.
- **Strike** (10 pins on the 1st roll): frame ends after 1 roll; frame score = 10 + pins knocked down on the *next 2 rolls*.
- **10th frame**: a spare or strike earns one or two extra fill balls respectively, for a maximum of 3 rolls in that frame; those fill rolls count only toward the 10th frame's bonus, not as extra frames.

This is the full and only spec driving `roll`/`score` — implement strictly via TDD (red-green-refactor) against these rules.
