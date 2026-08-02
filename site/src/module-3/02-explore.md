---
order: 2
title: Explore
kicker: Module 3 · Part 2
standfirst: >
  Find out what you have been handed before you change any of it. Shape, types, ranges, what is missing, and what the categories actually contain.
status: scaffold
prev:
  url: /module-3/01-understand/
  label: Part 1 · Understand
next:
  url: /module-3/03-prepare/
  label: Part 3 · Prepare
---

<!-- authoring note: template — cold open, concept, do it, compare. -->

{% todo "Cold open" %}
A number that should take ten seconds to look up, and does not.
{% endtodo %}

{% section "Get a feel for it" %}

{% slot "activity", "Concept level, away from the keyboard. The same thing written more than one way, counted as more than one thing." %}

### Think it through

{% todo "Check yourself · 2–3 questions" %}
Arguable. These are the discussion if the class is running together.

What should land: the difference between a value being wrong and a value being inconsistent; that scrolling through rows will never surface this; that counting the values in a column is the habit that does.
{% endtodo %}

{% section "Before your first run" %}

{% todo %}
The mechanics, the first time they are needed.
{% endtodo %}

{% slot "video", "Susan's Colab walkthrough. Copying to your own Drive, turning off Colab's built-in AI assistance, line numbers, sessions.", "180px" %}

{% callout %}
**If anything stops working:** Runtime → Restart session and run all. Try that before you debug
anything else.
{% endcallout %}

### The ground rules

Paste this at the start of any AI session for this module. It covers how the AI should work with
you, whatever the task is, and it is a decent example of a careful prompt.

<pre class="prompt">I'm a student learning data analysis. I'll be asking you to help me write
Python and pandas code for a dataset I'm working with. Some ground rules:

- Create new DataFrames rather than modifying existing ones in place, so I
  can re-run cells without corrupting my data.
- Before any operation that removes or changes rows, tell me how many rows
  it will affect.
- If what I ask for is ambiguous, ask me a question instead of guessing.
- Write the code I ask for. Don't decide what the analysis should be.</pre>

{% todo %}
One sentence on why the first rule matters. You will need a Google account for Colab and access
to a free AI chat tool.
{% endtodo %}

{% section "Do it for real" %}

{% todo "Name the job" %}
Find out what is in this file. Change nothing yet — the fixing is the next part.
{% endtodo %}

{% notebook "Notebook 1 — Explore" %}
Starts from a clean copy, so you can work this part whatever happened in an earlier one.

{% todo "To build" %}
- Space for your own prompt
- Space to paste and run what comes back
- Space to write down what you checked
{% endtodo %}
{% endnotebook %}

{% checklist "How to know it worked" %}
- Do you know what one row represents?
- Have you counted the values in every column that holds categories?
- Do you know how much is missing, and from where?
- Have you written down what looks wrong, without fixing any of it yet?
{% endchecklist %}

{% section "How a practitioner did it" %}

{% slot "video", "Habiba. Her first-look routine on an unfamiliar file, and what she checks before anything else.", "180px" %}

{% todo "The practitioner's version" %}
Their profiling pass, framed as one defensible way through.
{% endtodo %}

{% compare %}
| | You | The practitioner |
|---|---|---|
| Did it come out right? | | |
| How long did it take, including checking? | | |
| Could you explain every step? | | |
| What happens when the next file arrives? | | |
| How would you find out if it broke? | | |

{% todo %}
An AI will profile a file quickly and well. Knowing which of its findings matter is the part it cannot do.
{% endtodo %}
{% endcompare %}

{% todo "Facilitation notes" %}
Timing, what to poll the room on, which question is worth arguing about.
{% endtodo %}
