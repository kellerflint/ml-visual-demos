---
order: 2
title: Clean it
kicker: Module 3 · Part 1
standfirst: >
  The director asks for a number that should take ten seconds. Getting it right turns out to need a dozen decisions nobody told you you were making.
status: scaffold
prev:
  url: /module-3/01-the-job/
  label: The job
next:
  url: /module-3/03-transform/
  label: Part 2 · Reshape it
---

<!-- authoring note: Phase 1 -> 3 -> 4. Concept, then do it, then compare. -->

{% todo "Cold open" %}
A situation with a decision in it. No definitions, no "in this part you will learn."
{% endtodo %}

{% section "Get a feel for it", "~30 min" %}

{% slot "activity", "Concept level, away from the keyboard. Should get the student to commit to an answer and be wrong." %}

### Think it through

{% todo "Check yourself · 2–3 questions" %}
Arguable. These are the discussion if the class is running together.

What should land: the difference between a value being wrong and a value being inconsistent; that collapsing categories is a decision; that a fix which silently drops data is worse than one that fails loudly.
{% endtodo %}

{% section "Before your first run", "~15 min" %}

{% todo %}
The mechanics, the first time they are needed.
{% endtodo %}

{% slot "video", "Susan's Colab walkthrough. Copying to your own Drive, turning off Colab's built-in AI assistance, line numbers, sessions.", "180px" %}

{% callout %}
**If anything stops working:** Runtime → Restart session and run all. Try that before you debug
anything else.
{% endcallout %}

### The ground rules

Paste this at the start of any AI session for this module. It covers how the AI should work
with you, whatever the task is, and it is a decent example of a careful prompt.

<pre class="prompt">I'm a student learning data analysis. I'll be asking you to help me write
Python and pandas code for a dataset I'm working with. Some ground rules:

- Create new DataFrames rather than modifying existing ones in place, so I
  can re-run cells without corrupting my data.
- Before any operation that removes or changes rows, tell me how many rows
  it will affect.
- If what I ask for is ambiguous, ask me a question instead of guessing.
- Write the code I ask for. Don't decide what the analysis should be.</pre>

{% todo %}
One sentence on why the first rule matters — it is a prompting habit that happens to prevent
the most common way a notebook gets into a state you cannot recover from.

You'll need a Google account for Colab and access to a free AI chat tool. Nothing to install.
{% endtodo %}

{% section "Do it for real", "~35 min" %}

{% todo "Name the job" %}
The data needs cleaning before anything else will work. Working out what that means here is the exercise.
{% endtodo %}

{% notebook "Notebook 1 — Clean it" %}
Starts from a clean copy, so you can work this part whatever happened in an earlier one.

{% todo "To build" %}
- Space for your own prompt
- Space to paste and run what comes back
- Space to write down what you checked
{% endtodo %}
{% endnotebook %}

{% checklist "How to know it worked" %}
- Count the values in every column you changed. Did a category disappear?
- Compare the row count before and after. Can you account for every row you lost?
- Check what became empty. Was that supposed to happen?
- Pick a value you know is in there and check it survived
{% endchecklist %}

{% section "How a practitioner did it", "~15 min" %}

{% slot "video", "Habiba, ~3 min. A messy column from real work. What she actually did about it, and who she had to ask.", "180px" %}

{% todo "The practitioner's version" %}
Their cells, framed as one defensible way through. Doubles as the recovery path for anyone
whose notebook is beyond saving.
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
This part should surface where the difficulty actually sits.
{% endtodo %}
{% endcompare %}

{% todo "Facilitation notes" %}
Timing, what to poll the room on, which question is worth arguing about.
{% endtodo %}
