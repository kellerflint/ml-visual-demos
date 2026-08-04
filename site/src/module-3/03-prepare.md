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

Cleaning one column, start to finish. Sort the clinic file's 14 spellings of gender into the three categories the analysis needs, and watch what happens to the ones you miss.

{% activity "p3b-label-machine.html", "The label machine", "640px" %}

{% check "Think it through before you open the answers." %}

{% q "Your map handles 13 of the 14 spellings and you run it. Nothing errors. What happened to the rows with the 14th spelling?" %}
They are still there, and their gender is now missing. A pandas `.map()` turns any value it has no rule for into `NaN`, silently. Thirteen right rules and one gap means the run looks perfect, the counts look plausible, and a slice of real patients has quietly left every gender breakdown you will ever make. This is why the check after a mapping is always the same. Count the values before, count them after, and make the totals match. A fix that fails loudly is a gift. The dangerous ones succeed.
{% endq %}

{% q "The AI merges Commercial into Private and self-pay into Uninsured without being asked. Both merges happen to be right. What is still wrong?" %}
Nobody decided. Whether Commercial insurance counts as Private is a fact about this clinic's billing, and the AI does not know this clinic. It pattern-matched what those words usually mean, got lucky, and buried the call inside working code. The next merge it invents may be wrong in a way nobody catches, because merges do not error. The fix is in how you ask. Spell out the target categories and every mapping in the prompt, so the AI types them and you own them.
{% endq %}

{% endcheck %}

{% section "Do it for real" %}

The job. Take the raw file and your Part 2 quality report, fix every problem on the list, then build the six columns the analysis ahead needs. Every fix that loses or changes a row gets a line in your decision log saying what you did and why.

{% notebook "Notebook 2 · Prepare", "https://colab.research.google.com/github/kellerflint/ml-visual-demos/blob/main/notebooks/m3-prepare.ipynb" %}
Starts from the raw file, so this part works whatever happened in your Part 2 notebook. Six jobs take you from duplicates through the new columns, and the date job is designed to fail on the first try. That failure is part of the lesson, and the notebook walks you through reading it.
{% endnotebook %}

{% checklist "How to know it worked" %}
- Count the values in every column you changed. Did a category disappear?
- Compare the row count before and after. Can you account for every row you lost?
- Look at the spread of every column you made
- For any yes/no flag, check what share of rows it covers. Does it still single anyone out?
{% endchecklist %}

{% section "How a practitioner did it" %}

{% slot "video", "The practitioner. A messy column and a derived column from real work. What they did, and who they had to ask.", "180px" %}

Then hold your work next to theirs, twice.

**How they decide against how you decided.** Watch what they do when a fix needs a judgment call. Some calls they make from the data, and some they take to a person, and knowing which is which is the skill on display. Compare that to your decision log. Which of your calls did you make alone that they would have taken to somebody?

**Their decision log against yours.** Find one call the two of you made differently, dropped against kept, merged against separate, and trace what your version does downstream that theirs would have done differently. If their reasoning is better, your log is one line longer now, and that is the log working.

An AI will happily pick your thresholds and your mappings for you. Picking them is the actual job, and the prompt is where you do it.
