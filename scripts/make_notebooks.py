"""Author the Module 3 notebooks.

Notebooks are data, and hand-editing JSON invites drift, so every notebook is
generated here and committed. Regenerate after edits:

    python3 scripts/make_notebooks.py

STATUS: these are deliberately placeholders. The full six-job versions of
notebooks 1 through 4 are preserved on the `full-build-archive` branch. They
were cut because how technique gets taught in this module is an open question
that belongs to the practitioner who will write these, not to the scaffolding.

What each notebook keeps: a working setup cell that loads the real hosted CSV,
so the "open in Colab" link works end to end and the format is demonstrable.
Everything after the setup cell is open space.
"""

import json
import os

RAW_URL = (
    "https://raw.githubusercontent.com/kellerflint/ml-visual-demos/"
    "main/site/src/data/outpatient_visits.csv"
)
CLEAN_URL = (
    "https://raw.githubusercontent.com/kellerflint/ml-visual-demos/"
    "main/site/src/data/outpatient_visits_clean.csv"
)
AUSTIN_URL = (
    "https://raw.githubusercontent.com/kellerflint/ml-visual-demos/"
    "main/site/src/data/austin_intakes_2024.csv"
)

_id = 0


def md(source):
    global _id
    _id += 1
    return {
        "cell_type": "markdown",
        "id": f"cell-{_id:03d}",
        "metadata": {},
        "source": source.strip().split("\n"),
    }


def code(source):
    global _id
    _id += 1
    return {
        "cell_type": "code",
        "id": f"cell-{_id:03d}",
        "metadata": {},
        "execution_count": None,
        "outputs": [],
        "source": source.strip().split("\n"),
    }


def write(path, cells):
    nb = {
        "cells": [
            {**c, "source": [line + "\n" for line in c["source"][:-1]]
             + c["source"][-1:]}
            for c in cells
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.11"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    with open(path, "w") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f"wrote {path}: {len(cells)} cells")


PLACEHOLDER = md("""
## This notebook is a placeholder

The setup cell below is real and loads the actual file, so the Colab link works
end to end. Everything after it is open space.

**A note for whoever writes this part.** How the technique gets taught here has
not been decided. It could be a recorded walkthrough, prose in these cells,
worked examples the student modifies, or nothing beyond the job statement on the
lesson page and an empty notebook. Each of those produces a different notebook,
so this one stays empty until that call is made.
""")

GROUND_RULES_NOTE = md("""
**Before anything else.** Open your AI chat and paste the ground-rules prompt
from the Part 2 page. Every prompt you write in this notebook goes into that
same conversation.
""")

WORKSPACE = [
    md("## Your work starts here"),
    code("\n"),
    code("\n"),
    code("\n"),
]


def notebook(title, scenario, deliverable, url, setup_note=None):
    """A placeholder notebook: framing, working setup cell, open space."""
    return [
        md(f"""
# {title}

{scenario}

**What you leave with.** {deliverable}
"""),
        PLACEHOLDER,
        GROUND_RULES_NOTE,
        md(f"""
## Setup

{setup_note or "Run this cell as it is. It loads the file straight from the course repository, so there is nothing to download or upload."}
"""),
        code(f"""
import pandas as pd

url = "{url}"
df = pd.read_csv(url)
print(f"Loaded {{df.shape[0]}} rows and {{df.shape[1]}} columns")
"""),
    ] + WORKSPACE


def explore():
    return notebook(
        "Module 3 · Notebook 1 · Explore",
        "You are the data analyst at a community outpatient clinic. The director "
        "wants two years of visit data understood, and the file was entered by "
        "many hands over those two years. This notebook is the first look. You "
        "change nothing.",
        "A written record of what is in this file and what looks wrong with it. "
        "Part 3 fixes what it lists.",
        RAW_URL,
    )


def prepare():
    return notebook(
        "Module 3 · Notebook 2 · Prepare",
        "Same clinic file, and now you have a list of what is wrong with it. "
        "This notebook fixes what the list holds and builds the columns the "
        "analysis ahead needs.",
        "A clean file, and a log of every decision you made to get it.",
        RAW_URL,
        "Run this cell as it is. It starts from the raw file, so this notebook "
        "works whatever happened in your Part 2 notebook.",
    )


def analyze():
    return notebook(
        "Module 3 · Notebook 3 · Analyze",
        "The clinic file is clean and the director is waiting on answers. This "
        "notebook is the two jobs together, every time. Get the answer, then "
        "find out who the answer is about.",
        "Answers to the director's questions, each one carrying the check that "
        "says who it covers and who it misses.",
        CLEAN_URL,
        "Run this cell as it is. It loads the course's cleaned file, the output "
        "of Part 3, so everyone analyzes identical data.",
    )


def share():
    return notebook(
        "Module 3 · Notebook 4 · Share",
        "The director reads one thing, and it is short. This notebook turns "
        "your findings into the version that gets read.",
        "Four sentences and one limitation, every claim traceable to a number "
        "you produced.",
        CLEAN_URL,
        "Run this cell as it is. It loads the cleaned clinic file so your "
        "numbers come from the same place your findings did.",
    )


def build():
    return notebook(
        "Module 3 · Notebook 5 · From scratch",
        "A different shelter, a different manager, a different question, and no "
        "guardrails. Every animal that came through Austin's city shelter in "
        "2024, straight from the city's open data portal, published by the city "
        "and untouched by us.",
        "The whole loop, alone. A brief, a quality report, a decision log, "
        "answers with their checks, and four sentences for the manager.",
        AUSTIN_URL,
        "Run this cell as it is, and then the blankness is the point. "
        "Everything after it is yours.",
    )


if __name__ == "__main__":
    os.makedirs("notebooks", exist_ok=True)
    write("notebooks/m3-explore.ipynb", explore())
    write("notebooks/m3-prepare.ipynb", prepare())
    write("notebooks/m3-analyze.ipynb", analyze())
    write("notebooks/m3-share.ipynb", share())
    write("notebooks/m3-build.ipynb", build())
