---
order: 4
title: Analyze
kicker: Module 3 · Part 4
standfirst: >
  Answer the question you settled on in Part 1, then work out who is missing from the answer before anyone acts on it.
prev:
  url: /module-3/03-prepare/
  label: Part 3 · Prepare
next:
  url: /module-3/05-share/
  label: Part 5 · Share
---

The director wants to know which county sends the clinic the most patients. One line of pandas answers it. Los Angeles, 85 visits, top of the list.

Here is what the one line skips. Nearly a third of the visits in the file have no county at all. The ranking you just produced describes the 70% of visits where somebody wrote the county down, and it is only the answer if the missing third looks like the recorded two thirds. Whether it does is checkable, and almost nobody checks. This part is the two jobs together, every time. Get the answer, then find out who your answer is about.

{% section "Get a feel for it" %}

Ask the clinic data anything, and before the answer appears, commit to what you expect. The gap between what you expected and what comes back is where analysis actually happens, and one of these answers has a hole in it big enough to sink a report.

{% activity "p4a-missing-on-purpose.html", "Missing on purpose", "680px" %}

{% check "Think it through before you open the answers." %}

{% q "County is missing on 16% of Uninsured visits and 36% of Medicaid visits. Most people guess the reverse. Why is the direction worth knowing before you trust any county number?" %}
Because it tells you the missingness has a cause, and the cause decides what the numbers mean. Gaps that follow a group are gaps with a reason, an intake form, a billing system, a workflow, and data missing for a reason distorts whatever that reason touches. Any county breakdown here quietly underweights Medicaid patients, the clinic's largest group. And the surprise itself is the lesson. If you had assumed the direction instead of checking it, you would have explained a pattern that runs the other way.
{% endq %}

{% q "A colleague says the fix is simple, drop the rows with no county. The percentages will be computed cleanly then. What did the fix just do?" %}
It made the distortion permanent and invisible. The dropped rows were 36% of Medicaid visits and 16% of Uninsured ones, so the cleaned dataset now underrepresents Medicaid patients everywhere, in every table, chart, and average built from it, with no missing values left to warn anyone. The gap used to announce itself. Now it is baked in. Dropping missing data is only safe when the missing rows look like the kept ones, and that is exactly what the missingness check just told you is false here.
{% endq %}

{% endcheck %}

{% section "Do it for real" %}

The job. Answer the director's five questions, and attach to each answer the check that says who it is about. Both halves go in your notebook. The questions come from the original analysis plan for this dataset. Top diagnoses, frequent visitors, seasonal patterns, diagnosis by age group, and the gaps between visits.

{% notebook "Notebook 3 · Analyze", "https://colab.research.google.com/github/kellerflint/ml-visual-demos/blob/main/notebooks/m3-analyze.ipynb" %}
Loads the course's cleaned file, the output of Part 3, so everyone analyzes identical data. Five director questions, each with a write-your-expectation-first habit built in, then the who-is-missing pass on your own answers.
{% endnotebook %}

{% checklist "How to know it worked" %}
- Does your number answer the question that was asked, or an easier one nearby?
- Check what every percentage is a percentage *of*, and put the group size next to it
- Read your own chart as a stranger would. What would you conclude?
- Ask whether a gap comes from how the data was collected or from what it describes
{% endchecklist %}

{% section "How a practitioner did it" %}

{% slot "video", "The practitioner. The most valuable recording in the module. A time missing data turned out to mean something: how they worked out which kind of missing it was, and who they asked.", "180px" %}

Then hold your work next to theirs, twice.

**Their suspicion against yours.** They tell a story about missing data that turned out to mean something. Notice the moment they stopped trusting the number, what tipped them off, what they checked next, and who they went to ask. Compare that to your own missingness check. Did anything in your Job 6 output deserve the follow-up they would have given it?

**Their caveat against yours.** They had to tell somebody what the data could and could not support, the same sentence you wrote at the end of the notebook. Put yours next to how they handled it. Does your caveat name a number, a consequence, and a next step, or does it hedge in general terms? Rewrite yours now if theirs exposes it, because Part 5 sends it to the director.

AI is good at making charts and at listing things to check. Deciding what is worth plotting, and what a gap means at this particular clinic, is the part that still needs a person who can ask.
