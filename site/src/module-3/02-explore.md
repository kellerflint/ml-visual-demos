---
order: 2
title: Explore
kicker: Module 3 · Part 2
standfirst: >
  Find out what you have been handed before you change any of it. Shape, types, ranges, what is missing, and what the categories actually contain.
prev:
  url: /module-3/01-understand/
  label: Part 1 · Understand
next:
  url: /module-3/03-prepare/
  label: Part 3 · Prepare
---

The director asks what sounds like the easiest question in the building. How many
visits did we get last year?

The file has 812 rows, so the ten-second answer is 812. It is wrong three ways at
once. Fifteen of those rows are the same visit entered twice. Four of the dates
never happened, February 30th among them. And "last year" means filtering on a
date column that is still text, written three different ways. The easiest
question in the building already depends on knowing exactly what is in the file.

Finding that out is this part's whole job. You change nothing. You count what is
in every column and write down every problem you find. The fixing happens in
Part 3, and it goes fast once you know what needs fixing.

{% section "Get a feel for it" %}

This is the real clinic file, all 812 rows of it, hooked up to the five checks
every profiler runs on a new dataset. Six defects are hiding in the data. Find
all six, and pay attention to which check catches each one, because in the
notebook below you will be asking an AI to run these exact checks.

{% activity "p2c-profilers-toolkit.html", "The profiler's toolkit", "660px" %}

{% check "Think it through before you open the answers." %}

{% q "The gender column contains f, F, female, Female, and FEMALE. Every one of those rows records a real patient correctly. So what is the problem?" %}
No single value is wrong. The column disagrees with itself, and software takes
the disagreement literally. A count of patients by gender returns five rows of
"female." A filter on `'Female'` quietly keeps one spelling and drops the other
four. The patient was recorded correctly and the analysis still comes out wrong,
which is why inconsistency is its own category of problem, separate from error.
It also explains the fix ahead of time. An error you correct. An inconsistency
you standardize.
{% endq %}

{% q "You scroll the first hundred rows and everything looks fine. What have you learned about the file?" %}
Almost nothing, and the math says so. Four bad dates in 812 rows means a random
hundred rows will usually contain zero of them. Thirty-three missing ages are
easy to scroll past. Fifteen duplicated rows look like ordinary rows unless
their twin happens to sit on screen at the same time. Problems this sparse live
in the file's totals, and totals only show up when you count. That is why a
practitioner's first move is a census of every column, and why "it looked fine
when I opened it" convinces nobody.
{% endq %}

{% endcheck %}

{% section "Before your first run" %}

You need two things for the rest of this module. A Google account, for Colab.
And a free AI chat tool, any of the major ones.

{% slot "video", "A Colab walkthrough. Copying to your own Drive, turning off Colab's built-in AI assistance, line numbers, sessions.", "180px" %}

{% callout %}
**If anything stops working:** Runtime → Restart session and run all. Try that
before you debug anything else.
{% endcallout %}

### The ground rules

Paste this at the start of any AI session for this module. It covers how the AI
should work with you, whatever the task is, and it is a decent example of a
careful prompt.

<pre class="prompt">I'm a student learning data analysis. I'll be asking you to help me write
Python and pandas code for a dataset I'm working with. Some ground rules:

- Create new DataFrames rather than modifying existing ones in place, so I
  can re-run cells without corrupting my data.
- Before any operation that removes or changes rows, tell me how many rows
  it will affect.
- If what I ask for is ambiguous, ask me a question instead of guessing.
- Write the code I ask for. Don't decide what the analysis should be.</pre>

The first rule earns its place the first time you re-run a cell. Notebook cells
run in any order, as many times as you click them, and a cell that overwrites
your data does its work again on every click. Two runs of a cell that halves
the file leaves a quarter of the file. New DataFrames make every cell safe to
run twice.

{% section "Do it for real" %}

The job. Find out what is in this file and write down every problem, in a
notebook, with an AI writing the code from your prompts. Change nothing yet.
The fixing is Part 3.

{% notebook "Notebook 1 · Explore", "https://colab.research.google.com/github/kellerflint/ml-visual-demos/blob/main/notebooks/m3-explore.ipynb" %}
Loads the clinic file for you and walks the census in six jobs, from first look
to date formats. For each job you write the prompt, run what comes back, and
check it before you trust it. The notebook tells you what each prompt has to
pin down. It never hands you the prompt.
{% endnotebook %}

{% checklist "How to know it worked" %}
- Do you know what one row represents?
- Have you counted the values in every column that holds categories?
- Do you know how much is missing, and from where?
- Have you written down what looks wrong, without fixing any of it yet?
{% endchecklist %}

{% section "How a practitioner did it" %}

{% slot "video", "The practitioner. Their first-look routine on an unfamiliar file, and what they check before anything else.", "180px" %}

Then hold your work next to theirs, twice.

**Their routine against yours.** They check things in an order, and the order
has reasons. What do they look at first, and why that first? Which of their
checks did you never think to run, and which of yours did they skip? Their
routine is the product of every file that has burned them. Yours is one file
old. The gap between them is a list of things worth stealing.

**Their quality report against yours.** Same file, two problem lists. What did
they flag that you missed, and what did you flag that they passed over without
a note? The second kind is as interesting as the first, because it usually
means they know something about data like this that makes the oddity
ordinary.

An AI profiles a file quickly and well. Deciding which of its findings matter,
and which are ordinary for data like this, is the part that still belongs to
whoever knows the clinic.
