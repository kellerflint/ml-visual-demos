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

{% todo "To write" %}
The job statement for this part, the way Parts 1 and 2 state theirs.
{% endtodo %}

{% slot "notebook", "The notebook for this part, opening in Colab the way Part 2's does. It starts from the raw file, so this part works whatever happened in your Part 2 notebook.", "180px" %}

{% section "How a practitioner did it" %}

{% slot "video", "The practitioner. A messy column and a derived column from real work. What they did, and who they had to ask.", "180px" %}

{% todo "To write" %}
The two comparisons the student makes against the recording, chosen for this part.
{% endtodo %}

{% feedback "3", "3" %}
