---
order: 5
title: Share
kicker: Module 3 · Part 5
standfirst: >
  Four sentences for someone who will only ever read the summary. The AI writes them better than you do, using only your numbers, and you should still hold some of them back.
prev:
  url: /module-3/04-analyze/
  label: Part 4 · Analyze
next:
  url: /module-3/06-build/
  label: Do it from scratch
---

Here is a sentence about the clinic, and every number in it is correct.

> High utilizers drive 74% of clinic visits, showing that a small group of
> patients is responsible for most of the workload.

You verified both numbers yourself in Part 4. And the sentence is wrong. The
"small group" is 110 patients, over half the panel, flagged by a threshold
somebody defaulted to. The word *showing* smuggles in a conclusion, and the
word *small* smuggles in a falsehood, and a director who reads this sentence
plans a program for the wrong clinic. Numbers can all be right while the
sentence lies. This part is about the sentence.

{% section "Get a feel for it" %}

An AI drafted a summary of your Part 4 findings for the director. It reads
well. Go through it sentence by sentence and decide, for each claim, whether
your data supports it. Every number in the draft appears in your own notebook
output, which is exactly what makes the bad sentences hard to catch.

{% activity "p5a-red-pen.html", "The red pen", "700px" %}

{% check "Think it through before you open the answers." %}

{% q "One flagged sentence had a correct number and a wrong verb. Why is the verb where summaries go wrong?" %}
A number is a measurement. A verb like *shows*, *drives*, or *causes* is a
claim about the world, and the data usually supports the measurement while
falling far short of the claim. Visit counts and follow-up rates can coexist
with almost any story about why. The honest verbs are quieter. *Is*, *has*,
*averaged*, *ranged*. When a summary needs a stronger verb, the support has to
come from somewhere beyond the table, and the reader deserves to know where.
{% endq %}

{% q "The draft's most dangerous sentence was the one you had no way to check. What made it dangerous, and what is the fix?" %}
It was plausible, it fit the story, and it referenced nothing you computed, so
there was no receipt to pull. A claim without a receipt in a summary full of
receipts borrows credibility from its neighbors, and the borrowing works,
which is how invented details survive review. The fix is mechanical and a
little ruthless. Every claim gets traced to a number you produced, and a claim
with no source gets cut, whatever it adds to the story. Verification is per
claim, and it transfers to nothing.
{% endq %}

{% endcheck %}

{% section "Do it for real" %}

The job. Turn your Part 4 findings into four sentences and one limitation for
the director, with an AI drafting and you fact-checking. Write your own four
sentences first, before the AI sees anything. It will feel skippable and it is
the load-bearing step, because your version is what makes the AI's errors
visible to you.

{% notebook "Notebook 4 · Share", "https://colab.research.google.com/github/kellerflint/ml-visual-demos/blob/main/notebooks/m3-share.ipynb" %}
Builds the verified stat block from the clean file, has you write yours, then
has the AI draft under a numbers-only constraint. The fact-check walks claim
by claim, and the deliverable is the version you would actually send.
{% endnotebook %}

{% checklist "How to know it worked" %}
- Every number in the draft is one of yours. Check each one.
- Every verb is one your data can support
- Any average comes with something about the spread
- Read it as the director. What would you do next? Is that supported?
{% endchecklist %}

{% section "How a practitioner did it" %}

{% slot "video", "The practitioner. When is AI worth skipping? Their rubric with examples.", "180px" %}

Then hold your work next to theirs, twice.

**What they use AI for against what you did.** Their rubric is a working
professional's answer to where AI belongs in their own writing process, drawn
before you had to make the same calls in Notebook 4. Where does their line sit
compared to where you drew yours? If they skip AI somewhere you leaned on it,
their reason is the interesting part.

**What got left out.** A four-sentence summary is mostly the things it
declines to say. Compare what you cut against what a practitioner cuts, the
tempting number with no receipt, the finding that needs a threshold to mean
anything. If your final version kept something their rubric would have
flagged, that is the sentence to reread before anything goes to a director.

Drafting is where the AI helped most in this whole module, and the summary is
the one artifact the director acts on, so it is also where an unchecked error
costs most. Both things are true, and holding both at once is the skill this
part practices.
