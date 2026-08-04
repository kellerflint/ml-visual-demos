---
order: 6
title: Do it from scratch
kicker: Module 3 · On your own
standfirst: >
  A dataset that is new to you, a real question, and your own judgment about how to approach it.
  Everything up to here was practice with the guardrails on.
prev:
  url: /module-3/05-share/
  label: Part 5 · Share
next:
  url: /module-3/
  label: Module 3 overview
---

A different inbox this time.

> **From:** Shelter Manager, Austin Animal Center
> **Subject:** council budget review
>
> The city council reviews our budget in October. Can you put together
> something on last year's intakes? I keep telling them we're stretched past
> capacity and it never lands. Whatever the data shows.

The data is real. Every animal that came through Austin's city shelter in
2024, from the city's public data portal, 11,817 rows exactly as the city
published them. Real data means the problems in it were made by real intake
software and real people on real days, and we are handing you the file the way
the manager would, with a request and no list of what is wrong with it.

Finding what is wrong with it is the work. So is deciding what the manager is
actually asking for, and what this file can honestly say about capacity, and
what it cannot. The file records animals coming in. Think about what that
means for a claim about being stretched.

{% section "The job" %}

The whole loop, alone. Understand the request, explore the file, prepare it,
answer the questions your brief settled on, and write the four sentences. Your
AI chat is open the whole time, the ground rules from Part 2 still apply, and
every prompt is yours to write.

{% notebook "Notebook 5 · From scratch", "https://colab.research.google.com/github/kellerflint/ml-visual-demos/blob/main/notebooks/m3-build.ipynb" %}
Loads the shelter file and stops. The blankness is the point. Everything that
goes in it after the first cell is yours.
{% endnotebook %}

{% section "What to hand in" %}

Four things, and every one has a Part behind it.

The brief, one page, built the way Part 1 built it. The quality report and
decision log for this file, the way Parts 2 and 3 kept them. Your answers with
their checks attached, the way Part 4 paired them. And four sentences with one
limitation for the manager, Part 5's shape, ready for a council packet.

{% checklist "Before you call it done" %}
- Could someone else read your brief and know when the work was finished?
- Can you account for every row you dropped, and every value you changed?
- Does each answer say who it is about, and who is missing from it?
- Is every claim in your four sentences traceable to a number in your notebook?
- What did you flag as a question for the shelter that the data could not answer?
{% endchecklist %}

{% section "Afterwards" %}

{% slot "notebook", "A worked version, released after hand-in. One defensible way through, with the reasoning visible.", "150px" %}

Two analysts who both did honest work on this file will still differ, because
they made different defensible calls. What they will have in common is that
you can trace every number in both, and that each would survive the other's
review. That is the standard, and after this page you have everything you need
to hold work to it.
