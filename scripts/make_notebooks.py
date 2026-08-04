"""Author the Module 3 notebooks.

Notebooks are data, and hand-editing JSON invites drift, so every notebook is
generated here and committed. Regenerate after edits:

    python3 scripts/make_notebooks.py

Conventions (see data-curriculum/REVIEW-FRAMEWORK.md, Gate 5):
- one phase per notebook, deterministic starting state from a hosted CSV
- students write their own prompts; each task gives the job and a spec of what
  the prompt must pin down, never the prompt itself
- verification is independent of the AI's output: row arithmetic, spot checks
  against the raw file, second computation paths
- markdown obeys the module voice rules
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


PASTE = "# Paste the AI's code here. Read it before you run it.\n"

GROUND_RULES_NOTE = md("""
**Before anything else.** Open your AI chat and paste the ground-rules prompt
from the Part 2 page. Every prompt you write in this notebook goes into that
same conversation.
""")


def job(n, title, the_job, spec, check):
    """One task block: job, prompt spec, paste cell, check cell guidance."""
    cells = [md(f"""
## Job {n} · {title}

{the_job}

**Your prompt has to pin down:**
{spec}
""")]
    cells.append(code(PASTE))
    cells.append(md(f"""
**Check it before you trust it.**

{check}
"""))
    return cells


# ---------------------------------------------------------------- notebook 1
def explore():
    cells = [
        md("""
# Module 3 · Notebook 1 · Explore

You are the data analyst at a community outpatient clinic. The director wants
two years of visit data understood, and the file was entered by many hands over
those two years. This notebook is the first look. You change nothing. You find
out what is in the file and write every problem down.

What you leave with: a written quality report. Part 3 fixes what it lists.
"""),
        GROUND_RULES_NOTE,
        md("""
## Setup

Run this cell as it is. It loads the clinic file straight from the course
repository, so there is nothing to download or upload.
"""),
        code(f"""
import pandas as pd

url = "{RAW_URL}"
df = pd.read_csv(url)
print(f"Loaded {{df.shape[0]}} rows and {{df.shape[1]}} columns")
"""),
    ]

    cells += job(
        1, "First look",
        "Find out what one row represents, what the columns are, and what type "
        "each column holds. Before you run anything, write down your guess for "
        "what one row is. A patient? A visit? Something else?",
        """
- the DataFrame is named `df`
- you want the first rows, the column types, and the non-null count per column
- ask for output you can read, with each check labeled
""",
        """
One row is one visit, and the same patient appears on many rows. Confirm that
from the output. Pick any `patient_id` you can see in the first rows and ask
for that patient's rows. If the file surprises you here, everything downstream
inherits the surprise.

Look at the type of `visit_date`. It is text, and that fact is a finding for
your report.
""",
    )

    cells += job(
        2, "The missing census",
        "Find out how much of the file is missing, column by column.",
        """
- count of missing values per column, and that count as a percent of all rows
- only columns that have missing values, sorted worst first
""",
        """
Cross-check one number by a second route. The output claims some count of
missing counties. Ask for the number of rows where `county` is present, add
the two, and the sum has to be the row count from Setup. If the sum is off,
one of the two numbers is lying, and finding out which one is exactly the
skill this module is for.
""",
    )

    cells += job(
        3, "The duplicate census",
        "Find out whether any rows appear more than once.",
        """
- count of exact duplicate rows
- show the duplicated rows next to their originals so you can eyeball a pair
""",
        """
Take one duplicated pair and look at every field. Identical rows, including
the `visit_id` that is supposed to be unique per visit, mean the same visit
was entered twice, and every count in the file is inflated by these rows
until Part 3 removes them. Write the count in your report.
""",
    )

    cells += job(
        4, "The category census",
        "Count every distinct value in the four columns that hold categories. "
        "This is the census the ten rows at the top of the Part 2 page were "
        "hiding. Before running, write down how many spellings of female you "
        "expect gender to contain.",
        """
- the four columns by name: `gender`, `insurance_type`, `visit_type`, `follow_up_required`
- every distinct value with its count, for each column, labeled
""",
        """
The counts inside each column have to sum to the row count from Setup, because
none of these four columns had missing values in Job 2. Check one column's sum.
Then compare what you predicted for gender against what you got, and write the
variant counts for all four columns in your report. Part 3 needs the full
lists, so keep this output.
""",
    )

    cells += job(
        5, "Out-of-range numbers",
        "Numbers can be present, well-formed, and impossible. Find any.",
        """
- summary statistics for the numeric columns, so minimums and maximums are on screen
- rows where `age` is below 0 or above 120
- rows where `copay_amount` is negative
""",
        """
The summary statistics and the row listings have to agree. If the minimum age
in the summary is negative, the age listing has to contain that row. Note what
the impossible values are, and notice the rows around them look ordinary. A
wrong field does not announce itself.
""",
    )

    cells += job(
        6, "The date census",
        "The `visit_date` column is text. Find out how many ways the dates are "
        "written, and whether any value fits no date format at all.",
        """
- the date is text in `visit_date`
- you expect shapes like 2023-08-04, 08/04/2023, and 08-04-2023
- count how many values match each shape, and show every value that matches none
""",
        """
The shape counts plus the misfits have to sum to the row count. Read the
misfit values out loud and write them in your report.

Two thoughts to carry into Part 3. First, a shape check believes anything with
the right shape, and whether every shape-matched value is a real date is a
different question. Second, look at a value like 08-04-2023 and answer for
yourself which day it names. Both questions come due the moment anyone tries
to parse this column.
""",
    )

    cells += [
        md("""
## The quality report

This is the deliverable. Edit this cell and fill it in from your outputs. Every
line needs a number you can point to in a cell above.

| Problem | Where | How big |
|---|---|---|
| Duplicate rows | whole file | |
| Missing values | (worst columns) | |
| Category spellings | gender / insurance / visit type / follow-up | |
| Impossible numbers | age, copay | |
| Date formats | visit_date | |
| Dates that fit no format | visit_date | |

**One row represents:**

**The thing I expected that was wrong:**

**The problem I would raise with the director first:**
"""),
        md("""
## Where this leaves you

The file is untouched, and you now know it better than anyone who has only
opened it. Part 3 fixes every line of your report, and each fix is a decision
somebody has to be able to defend later.
"""),
    ]
    return cells


if __name__ == "__main__":
    os.makedirs("notebooks", exist_ok=True)
    write("notebooks/m3-explore.ipynb", explore())
