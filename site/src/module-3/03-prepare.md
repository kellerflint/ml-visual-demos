---
order: 3
title: Prepare
kicker: Module 3 · Part 3
standfirst: >
  Now fix what you found, and build the columns your question needs. Both look like chores and are really a run of decisions.
prev:
  url: /module-3/02-explore/
  label: Part 2 · Explore
next:
  url: /module-3/04-analyze/
  label: Part 4 · Analyze
---

One of the dates in your quality report reads `2023-00-00`. The row it sits on is a real visit. It has a diagnosis, a provider, a copay of $0, a patient who was there. The date is the only broken thing on the row.

You have three honest options. Drop the row and lose a real visit. Keep the row and let one unparseable value crash every date operation downstream. Or set the date to missing and keep the rest, which saves the visit and quietly changes what "visits per month" means. There is no fourth option where the problem goes away, and an AI asked to "fix the dates" will pick one of the three without telling you which.

That is what preparing data is. A run of small decisions, each with a cost, made one column at a time and written down. This part you make them yourself.

{% section "Get a feel for it" %}

{% slot "activity", "An activity and two check questions, the shape Parts 1 and 2 use. The idea for this part is cleaning one column start to finish, so a fix that quietly drops rows is something the student feels before the notebook asks for one.", "200px" %}

{% section "Lessons" %}

{% slot "lesson", "The teaching content for this part goes here, between getting a feel for the idea and doing it for real. What form it takes is still open. A recorded walkthrough, written explanation on this page, worked examples the student modifies, or nothing beyond the job statement and an empty notebook.", "200px" %}

{% section "Do it for real" %}

The job. Take the raw file and your Part 2 quality report, fix every problem on the list, then build the six columns the analysis ahead needs. Every fix that loses or changes a row gets a line in your decision log saying what you did and why.

{% notebook "Notebook 2 · Prepare", "https://colab.research.google.com/github/kellerflint/ml-visual-demos/blob/main/notebooks/m3-prepare.ipynb" %}
Opens in Colab and starts from the raw file, so this part works whatever happened in your Part 2 notebook. Everything after that first cell is open space, waiting on the lesson format above.
{% endnotebook %}

{% section "How a practitioner did it" %}

{% slot "video", "The practitioner. A messy column and a derived column from real work. What they did, and who they had to ask.", "180px" %}

Then hold your work next to theirs, twice.

**How they decide against how you decided.** Watch what they do when a fix needs a judgment call. Some calls they make from the data, and some they take to a person, and knowing which is which is the skill on display. Compare that to your decision log. Which of your calls did you make alone that they would have taken to somebody?

**Their decision log against yours.** Find one call the two of you made differently, dropped against kept, merged against separate, and trace what your version does downstream that theirs would have done differently. If their reasoning is better, your log is one line longer now, and that is the log working.

An AI will happily pick your thresholds and your mappings for you. Picking them is the actual job, and the prompt is where you do it.
