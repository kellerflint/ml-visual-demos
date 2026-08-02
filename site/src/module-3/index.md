---
title: Preparing, Exploring & Analyzing Data with AI
kicker: AI in Data Science · Module 3
standfirst: >
  Most of data work happens before there is a number to look at. The judgment about whether to
  believe it happens after.
eleventyExcludeFromCollections: true
next:
  url: /module-3/01-understand/
  label: Start · Understand
prev:
  url: /
  label: All modules
---

<!-- authoring note: topic only; the clinic scenario starts in 01-the-job.
     Three beats, lifted from lessons/data-lessons.html:
       1  the journey   -> what this work is
       2  the planes    -> how data misleads
       3  almost right  -> how you check
     Activity files are the originals, copied into src/activities/. -->

Somebody asks you a question. You get handed a file. At the end of it, a number goes in front of
a person who is going to act on it.

Everything between those points is this module. Working out what the question actually is.
Finding out what you were handed before you change any of it. Fixing what's broken and building
the columns your question needs. Getting an answer, then working out who is missing from it.
Saying it in four sentences to someone who will only ever read the summary.

Every one of those steps is a decision, and you will be making them alongside an AI that decides
fast and sounds certain either way. Learning to direct that work, and to tell whether the result
holds up, is the job this module is about.

{% slot "video", "Module intro. The shape of the work and what you will build by the end.", "180px" %}

Start with the three activities below. Each one plants something you will use in every part that
follows: where a number comes from, how a dataset can mislead you while every value in it is
correct, and what it takes to check an answer that reads well. You can do all three with what is
on the screen. By the end of this page you will have met, in miniature, every problem the rest of
the module works through slowly.

{% section "One tap, one number" %}

Somewhere in Berlin, a customer taps *Buy*. Weeks later, a manager looks at a revenue chart and
makes a decision. Between those two moments, that one tap traveled through half a dozen systems.
Along the way it got reshaped by choices someone coded months ago. Follow it, one stop at a time.

{% activity "follow-the-record.html", "Follow the record", "620px" %}

{% check "Think it through before you open the answers." %}

{% q "At the cleaning stop, three things about the record were changed by choices someone coded: how money is written, how IDs are written, which region got attached. None of those choices were wrong. So why do data teams insist that every one of them be written down and reviewable?" %}
Because a different reasonable choice produces a different number. Count the euro order at
yesterday's exchange rate instead of today's, or match IDs slightly differently, and revenue
shifts. No bug anywhere. When two teams' numbers disagree, and they constantly do, the
explanation almost always lives in these invisible decisions rather than in anyone's arithmetic.
Writing the choices down, in code and in definitions everyone shares, turns "my spreadsheet says
something different" from a week-long argument into a five-minute diff. A number you can trust is
a number whose journey you can inspect.
{% endq %}

{% q "The manager's chart reads only the final summary table. It never touches the raw data. Give one reason that separation is deliberate, and one risk it creates." %}
**Why it's deliberate.** Raw data is messy, huge, and constantly changing shape. If every chart
read it directly, every chart would need its own cleaning logic, and they would all disagree.
Cleaning once, in the middle, gives everyone the same answer. It also keeps slow analytical
queries away from the systems running the actual business.

**The risk.** Distance. Everyone downstream silently inherits whatever choices the cleaning steps
made. If that logic is wrong, every chart built on it is wrong in the same convincing way, and the
person reading the dashboard has no way to see it. Trust concentrates in the middle of the
journey. That's exactly why the middle is where data teams put their tests.
{% endq %}

{% endcheck %}

{% section "The planes that didn't come back" %}

Every decision you just followed becomes visible once you go looking for it. Here is a way a
number goes wrong that stays invisible however carefully you check, because every value in the
data is correct.

World War II. Bombers return from missions over Europe full of holes, and the military maps every
hit, hoping to armor the planes better. Armor is heavy, so you can't protect everything. A
statistician named Abraham Wald was handed this data, and what he saw in it saved lives. Now you
get handed the same data. You have armor for two zones. Study the hit map and choose.

{% activity "armor-allocation.html", "Armor allocation", "620px" %}

{% check "Think it through before you open the answers." %}

{% q "Every dot on the hit map was real. Nobody made a measurement mistake. So where did the error live?" %}
In the population, not the measurements. The dataset was "hits on bombers *that returned*," and
it got quietly treated as "hits on bombers." The planes hit in the engines and cockpit mostly
never made it home to be measured. The most important evidence was structurally missing from the
table, and no amount of careful analysis *of the table* could reveal that. This is why
professionals interrogate a dataset with a question that sounds almost paranoid. *What would have
to happen for a record to end up in this data, and what kinds of records can never get in?*
{% endq %}

{% q "Your company surveys its current customers and scores 9 out of 10 on satisfaction. Explain why this might be the bomber problem wearing a business suit. Who are the planes that didn't come back?" %}
The survey only reaches customers who are still around to answer it. The angriest customers
already canceled. They're the shot-down planes, invisible in the data precisely *because* of the
thing you're trying to measure. A 9/10 from survivors is perfectly consistent with a company
hemorrhaging unhappy customers. The fix mirrors Wald's. Go looking for the missing population
instead of squeezing more analysis out of the survivors. That means exit interviews, outreach to
churned customers, and comparing the surveyed group against the full customer list. Once you know
this pattern you'll see it everywhere. Reviews come from people who didn't return the product.
Success stories come from businesses that didn't fold. Workout advice comes from people the
workout didn't injure.
{% endq %}

{% endcheck %}

{% section "Almost right" %}

So far, two ways a number goes wrong: decisions made inside the machinery, and a dataset that was
never complete to begin with. In this module you will be making both kinds of call with an AI
sitting next to you.

You will do data work with an AI assistant. Nearly everyone in the field already does. And in
survey after survey, the same professionals who use AI daily name the same frustration above all
the others. Answers that are *almost* right. Not wrong in ways that jump out. Wrong in ways that
read smoothly, sound confident, and cost you an afternoon when they slip through.

Getting answers out of AI is the easy part. The skill that matters is **review**, deciding with
evidence whether an answer is true. Below is a tiny orders table, small enough to check by eye. An
AI assistant has answered five questions about it. Some answers are solid. Some aren't. You're the
reviewer, and shipping a wrong number to your boss counts against you.

{% activity "review-queue.html", "Review queue", "660px" %}

{% check "Think it through before you open the answers." %}

{% q "The refund-rate mistake took you ten seconds to catch, because the table has 8 rows. At a real company it has 40 million rows and you can't eyeball anything. What does checking the AI's answer look like then?" %}
You stop checking the *answer* and start checking the *method*. Ask for the query and read it.
Does it filter to refunded orders, or count something else? Compute the number a second,
independent way and see if the two agree. Sanity-check against what you already know. If last
month's refund rate was 24% and the AI says 12.5%, something changed, either the business or the
math. Spot-check a sample by hand. Professionals also build these checks into the pipeline as
automated tests, so the checking happens every day instead of only when someone gets suspicious.
The reflex is the same one you practiced here. Only the tools scale up.
{% endq %}

{% q "Case 5 got the number right but invented a detail that wasn't in the data. Why is that arguably more dangerous than an answer that's plainly wrong?" %}
Because the true part buys trust for the false part. You verify the $70, feel done, and the
invented detail rides along into your report where someone might act on it. Plainly wrong answers
get caught by the first person who looks. A fabrication attached to a verified fact can survive
several rounds of review, because each reviewer assumes that checking *part* of the answer was
checking the answer. The lesson is that verification doesn't transfer. Every claim needs its own
receipt, especially the ones sitting next to a claim that checked out.
{% endq %}

{% endcheck %}

## What's ahead

Five parts, in the order the work actually happens. Each one has a short activity to build the
idea, a notebook where you do it on a real clinic dataset with an AI, and a recording of a working
data scientist doing the same task so you can see where your version differs from theirs. Then a
dataset you have never seen, a question, and no instructions.

<div class="cards">

<a class="lcard" href="{{ '/module-3/01-understand/' | url }}">
  <p class="num">Part 1</p>
  <h3>Understand</h3>
  <p>Somebody asks you a question. Working out what they actually need, and what would count as an answer, comes before anything you can type.</p>
  <div class="meta"><span><b>TBD min</b></span></div>
</a>

<a class="lcard" href="{{ '/module-3/02-explore/' | url }}">
  <p class="num">Part 2</p>
  <h3>Explore</h3>
  <p>Find out what you have been handed before you change any of it. Shape, types, ranges, what is missing, what the categories contain.</p>
  <div class="meta"><span><b>TBD min</b></span></div>
</a>

<a class="lcard" href="{{ '/module-3/03-prepare/' | url }}">
  <p class="num">Part 3</p>
  <h3>Prepare</h3>
  <p>Fix what you found, and build the columns your question needs. Both look like chores and are really a run of decisions.</p>
  <div class="meta"><span><b>TBD min</b></span></div>
</a>

<a class="lcard" href="{{ '/module-3/04-analyze/' | url }}">
  <p class="num">Part 4</p>
  <h3>Analyze</h3>
  <p>Answer the question, then work out who is missing from the answer before anyone acts on it.</p>
  <div class="meta"><span><b>TBD min</b></span></div>
</a>

<a class="lcard" href="{{ '/module-3/05-share/' | url }}">
  <p class="num">Part 5</p>
  <h3>Share</h3>
  <p>Four sentences for someone who will only ever read the summary. Every number correct and the meaning still wrong is the failure mode.</p>
  <div class="meta"><span><b>TBD min</b></span></div>
</a>

<a class="lcard" href="{{ '/module-3/06-build/' | url }}">
  <p class="num">On your own</p>
  <h3>Do it from scratch</h3>
  <p>A dataset that is new to you, a real question, and your own judgment about how to approach it.</p>
  <div class="meta"><span><b>TBD min</b></span></div>
</a>

</div>
