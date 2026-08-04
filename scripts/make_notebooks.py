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


# ---------------------------------------------------------------- notebook 2
def prepare():
    cells = [
        md("""
# Module 3 · Notebook 2 · Prepare

Your Part 2 quality report lists everything wrong with the clinic file. This
notebook fixes every line of it, then builds the six columns the analysis in
Part 4 needs. Each fix is a decision, and the deliverable is the fixed data
plus a decision log that says what you chose and why.

One rule for the whole notebook. Any step that removes or changes rows gets
checked with arithmetic before you move on. You know the raw file has 812 rows.
Every row you lose has to be accounted for.
"""),
        GROUND_RULES_NOTE,
        md("""
## Setup

Run this cell as it is.
"""),
        code(f"""
import pandas as pd

url = "{RAW_URL}"
df = pd.read_csv(url)
print(f"Loaded {{df.shape[0]}} rows and {{df.shape[1]}} columns")
"""),
    ]

    cells += job(
        1, "Duplicates",
        "Your report counted rows that appear twice. Remove the copies, keep "
        "the originals, and put the result in a new DataFrame named `df_clean`.",
        """
- work from `df` into a new DataFrame named `df_clean`
- remove exact duplicate rows only, keeping the first of each pair
- print the row count before and after
""",
        """
812 minus the duplicate count from your report has to equal the new row count
exactly. If it removed more than your report counted, the code dropped
something it should have kept, and you want to know that now rather than in
Part 4.

Decision log line: how many rows removed, and why they were safe to remove.
""",
    )

    cells += job(
        2, "The date column, first attempt",
        "Ask for the simplest thing. Convert `visit_date` to datetime. This "
        "attempt is going to fail, and the failure is worth reading slowly.",
        """
- convert the `visit_date` column of `df_clean` to datetime
- nothing else, this is the naive version on purpose
""",
        """
Run it and read the error message from the bottom up. It names the exact value
it choked on and the format it expected. Since pandas 2.0, `to_datetime` reads
the first value, locks onto that value's format, and applies it to every row.
Three formats in one column means the lock is wrong for two thirds of the file.

The AI's code did what you asked. What you asked for was impossible as asked.
Keep the error on screen and go to Job 3.
""",
    )

    cells += job(
        3, "The date column, decided",
        "Now make the real decisions. Your report found values like "
        "`Feb 30 2023`, `not recorded`, `13/45/2023`, and `2023-00-00`. Those "
        "rows are real visits with one broken field. Decide what happens to "
        "them, then parse the column so every surviving value is a datetime.",
        """
- parse mixed formats. Tell the AI the three shapes the column contains
- two-part dates like 08-04-2023 read as month first. Say so explicitly,
  because the AI has to pick one reading and it should be yours
- your policy for unparseable values: drop those rows, or keep them with the
  date set to missing. Pick one and put it in the prompt
- print how many rows were affected and the final row count
""",
        """
Arithmetic first. Four values in the file parse as nothing. If you dropped
them, your count fell by exactly 4. If you kept them as missing, the count
held and `visit_date` now has exactly 4 missing values. Any other number means
the code did something you did not decide.

Then spot-check the reading. Find a row that was `08-04-2023` and confirm it
parsed to August 4th, because you said month first. 174 rows of your
deduplicated file change month under the other reading, which is why the
choice went in the prompt instead of staying in the AI's head.

Decision log lines: your policy for the four, and the month-first call.

The course's cleaned file, which Parts 4 and 5 use, dropped the four rows and
reads two-part dates month first. Your log can differ. It just has to say so.
""",
    )

    cells += job(
        4, "Categories",
        "Three columns say the same things too many ways. gender has 14 "
        "spellings for 3 categories, insurance_type has 18 for 4, visit_type "
        "has 16 for 4. Standardize all three, and turn follow_up_required's "
        "ten variants into 1 and 0.",
        """
- every target category by name: gender to Female, Male, Other; insurance_type
  to Medicaid, Medicare, Private, Uninsured; visit_type to Office Visit,
  Telehealth, Follow-Up, Urgent Care; follow_up_required to 1 and 0
- every mapping spelled out, from your Part 2 category census. The two
  judgment calls are yours to state: the clinic's billing office confirms
  Commercial bills as Private, and self-pay means Uninsured
- values with no rule should stay visible, so ask for a count of unmapped
  values per column after mapping
""",
        """
Count the values in each column after the run. Three categories in gender,
four in insurance_type, four in visit_type, two in follow_up_required, and
zero unmapped. Then the arithmetic. Each column's counts have to sum to your
current row count, because none of these columns had missing values in the
raw file. A shortfall means the map missed a spelling and `.map()` erased it
without a sound. That silent erasure is the single most common cleaning bug
there is.

Decision log lines: the Commercial call and the self-pay call.
""",
    )

    cells += job(
        5, "Impossible numbers",
        "Your report found ages of -5 and 999, and negative copays. The rows "
        "are real visits. The values are not. Set the impossible values to "
        "missing and keep the rows.",
        """
- age outside 0 to 120 becomes missing, the row stays
- negative copay_amount becomes missing, the row stays
- print how many values changed in each column
""",
        """
Ten ages and fourteen copays, exactly, and the row count does not move at all.
Compare that to Job 1, where rows disappeared. Both are correct and they are
different operations. A duplicate row is wrong as a row. An impossible age is
one wrong field on a right row, and deleting the visit to fix the age would
throw away a diagnosis, a provider, and a copay that are all real.

Decision log line: impossible values nulled, rows kept.
""",
    )

    cells += job(
        6, "The new columns",
        "The fixing is done. Now build the columns Part 4's questions need. "
        "Six of them, all derived from data you already have.",
        """
- visit_month, visit_year, and a short month name, from visit_date
- age_group using bins 0-18, 19-35, 36-50, 51-65, 65+
- is_high_utilizer, true for patients with 4 or more visits in the file,
  attached to every row of that patient
- days_since_last_visit, days since that patient's previous visit, missing
  for a patient's first visit. The data has to be sorted by patient and date
  before this one, and the prompt should say so
""",
        """
Three checks, each fast.

Count age_group. The 0-18 bin holds about ten visits. Look at the actual ages
in it before you conclude the clinic treats children. Every one is exactly 18,
because the youngest patient in this file is 18 and the bin label promises
more than the data contains. Labels lie when nobody reads what is inside them.

Count is_high_utilizer. It flags over half the panel. A flag that covers most
patients is a definition problem, and 4-or-more was a choice somebody made.
Note it for Part 4, where high utilizers are one of the director's questions.

Count missing days_since_last_visit. It should equal the number of patients,
one first visit each. If it equals something else, the sort before the diff
went wrong, and gap numbers in Part 4 would be quietly scrambled.
""",
    )

    cells += [
        md("""
## The decision log

The second deliverable. Edit this cell so it reads true for your run.

| Decision | What I chose | Why |
|---|---|---|
| Duplicate rows | | |
| Unparseable dates | | |
| Two-part date reading | | |
| Commercial | | |
| self-pay | | |
| Impossible age and copay | | |
| High-utilizer threshold | | |

**Rows in, rows out:** 812 in, ____ out, every loss accounted for above.
"""),
        md("""
## Where this leaves you

The file is consistent, dated, and six columns richer, and every choice that
got it there is written down. Part 4 finally asks the director's questions.
It uses the course's cleaned file so that everyone analyzes identical data,
and your decision log is what makes your own version defensible.
"""),
    ]
    return cells


# ---------------------------------------------------------------- notebook 3
def analyze():
    cells = [
        md("""
# Module 3 · Notebook 3 · Analyze

The file is clean and the director is waiting. Five questions, and every
answer travels with the check that says who it is about.

One habit runs through this whole notebook. Before you run anything, write
down what you expect. An expectation costs ten seconds, and it is the only
way to notice when an answer should surprise you.
"""),
        GROUND_RULES_NOTE,
        md("""
## Setup

Run this cell as it is. It loads the course's cleaned file, the output of the
Part 3 pipeline, so everyone analyzes identical data. 793 visits, 19 columns,
including the six you built.
"""),
        code(f"""
import pandas as pd

url = "{CLEAN_URL}"
df = pd.read_csv(url)
print(f"Loaded {{df.shape[0]}} rows and {{df.shape[1]}} columns")
"""),
    ]

    cells += job(
        1, "What brings people in",
        "The director's first question. What are the clinic's most common "
        "diagnoses? Write down the top three you expect before you run "
        "anything. Then decide what to do with the 28 visits that have no "
        "diagnosis code and the 17 coded UNKNOWN, and say it in the prompt.",
        """
- the DataFrame in this notebook is named `df`. Your Part 3 chat may still
  think in `df_clean`, and a wrong name is the fastest way to get code that
  crashes or, worse, runs against the wrong data
- count visits per diagnosis using `icd_description`, top 10, largest first
- your policy for missing and UNKNOWN codes, stated, with their counts printed
""",
        """
Essential Hypertension leads with 94 visits, about one visit in eight. Check
the AI's top count against a second path, a plain `value_counts()` on the
same column. Then read your expectation next to the table. For most people
the surprise is how much chronic disease outweighs the coughs and colds, and
that surprise is a real finding about what this clinic is.
""",
    )

    cells += job(
        2, "The frequent visitors",
        "Second question. How much of the clinic's work comes from patients "
        "who keep coming back? Part 3 built `is_high_utilizer` for exactly "
        "this. Expectation first: what share of visits do you think the "
        "flagged patients account for?",
        """
- how many patients are flagged, and how many visits they account for
- both as counts and as shares of the totals
""",
        """
110 of 200 patients, 584 of 793 visits, 74%. Now say it carefully. The flag
is over half the panel, because the 4-or-more threshold was somebody's
default, so "high utilizers drive 74% of visits" is nearly a tautology here.
Any sentence you hand the director about this number should name the
threshold it depends on. You saw in Part 3 what moving it does.
""",
    )

    cells += job(
        3, "The seasonal question",
        "Third question. Does visit volume have a seasonal pattern the clinic "
        "should staff for? Expectation first, and be honest about it. Most "
        "people expect a winter surge.",
        """
- visits per month with both years pooled
- then the same thing split by year, side by side, because a pattern that
  appears in the pool has to show up in both years to be called seasonal
""",
        """
The pooled months have to sum to 793. Then look at the split. The pooled
range runs from 50 in September to 80 in November, which looks like a story,
and the two years disagree about most of it. September is the year-two dip
doing the work, and November is high in both years by a little. Two years is
two data points per month. The defensible sentence is modest, and writing
the modest sentence when the chart tempts you toward the exciting one is the
skill.
""",
    )

    cells += job(
        4, "Diagnosis by age group",
        "Fourth question. Do different age groups come in for different "
        "things? The `age_group` column from Part 3 does the work.",
        """
- a table of the top diagnoses against age_group, counts in the cells
- limit it to the top 5 or 6 diagnoses so the table is readable
""",
        """
Before you describe any pattern, open the 0-18 column and look at who is in
it. Ten visits, every one a patient aged exactly 18, because the file's
youngest patient is 18 and the bin label promises children the data does not
contain. Any sentence about pediatric patterns from this table would be
about ten visits by legal adults. The other groups are large enough to
compare, and the caution transfers to any small cell in any crosstab you
ever make.
""",
    )

    cells += job(
        5, "The gaps between visits",
        "Last of the five. When patients come back, how long do they take? "
        "`days_since_last_visit` was built for this. Expectation first.",
        """
- the average and the median gap, and why you want both on screen
- how many rows have no gap value, and what those rows are
""",
        """
Mean 129 days, median 99, and the difference is the finding. A long tail of
patients who vanish for a year pulls the mean a month past the typical
return. 200 rows have no gap because a first visit has nothing to be since,
so the number of empty gaps has to equal the number of patients. If it does
not, something upstream reordered the file. Which average goes in a report
depends on the question, planning staffing follows the median, and modeling
no-shows cares about the tail.
""",
    )

    cells += job(
        6, "Who is the answer about",
        "Every answer above silently assumes the data represents the clinic. "
        "Now check it. County is the test case, because a third of it is "
        "missing. Write your guess first: which insurance group do you think "
        "has the most missing counties?",
        """
- the share of visits with county missing, within each insurance_type
- sorted so the worst group is on top
""",
        """
Medicaid 36%, Private 35%, Medicare 27%, Uninsured 16%. Most people guess
Uninsured for the top, and it is last. The gap follows a workflow somewhere,
an intake form, a billing path, and the data cannot tell you which. Note
what this does to Job 1 through 5. Any county-level view underweights
Medicaid, the clinic's largest group, and dropping the missing rows would
lock that distortion in while hiding the warning.

The deliverable for this job is one sentence, the caveat you would attach to
any report built on this file. Write it in the cell below, and keep it. Part
5 uses it.
""",
    )

    cells += [
        md("""
**My caveat sentence** *(edit this cell)*:

> ...
"""),
        md("""
## Stretch · the artifact hiding in a clean column

Skip this unless the main work left you time. It uses the raw file, and it
shows something subtle. Standardizing can manufacture a pattern.

In the cleaned data, county is missing on 44% of visits from patients with
gender Other, against 25% for Male. That reads like an equity finding. Now
compute the same missing rate on the raw file, grouped by the raw gender
spelling before any cleaning. Two specific spellings carry almost all of the
gap, and the spellings that mean the same thing sit near the file average.

The pattern follows how the value was typed, which means it follows who or
what entered the record, some intake pathway that both wrote gender its own
way and skipped county. Standardizing merged that pathway's rows with
everyone else's and the fingerprint vanished. The equity finding is real in
the cleaned file and misleading about the clinic. Nothing in either file can
tell you which pathway it was. A person at the clinic can, and this is the
single best example in the module of why the analyst who asks questions
beats the one who only computes.
"""),
        code(f"""
# Stretch starter: the raw file, for the pre-cleaning view.
raw = pd.read_csv("{RAW_URL}")
# Group county-missing rate by the raw gender values and compare.
"""),
        md("""
## Where this leaves you

Five answers, each with its check, and a caveat that tells the director how
far to trust them. Part 5 is the hard part. Saying all of this in four
sentences to someone who will read nothing else.
"""),
    ]
    return cells


if __name__ == "__main__":
    os.makedirs("notebooks", exist_ok=True)
    write("notebooks/m3-explore.ipynb", explore())
    write("notebooks/m3-prepare.ipynb", prepare())
    write("notebooks/m3-analyze.ipynb", analyze())
