---
title: Preparing, Exploring & Analyzing Data with AI
kicker: AI in Data Science · Module 3
standfirst: >
  Most of the work in data isn't the analysis. It's everything that happens before the number
  exists, and the judgment about whether to believe it once it does.
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

{% todo "Opening" %}
Short. The shape of the work and the order of what is coming. A few paragraphs at most.
{% endtodo %}

{% section "One tap, one number" %}

Somewhere in Berlin, a customer taps *Buy*. Weeks later, a manager glances at a revenue chart
and makes a decision. Between those two moments, that one tap traveled through half a dozen
systems and got reshaped by choices a person coded months ago. Follow it — the whole journey,
one stop at a time.

{% activity "follow-the-record.html", "Follow the record", "620px" %}

{% check "Think it through before you open the answers — that's the whole exercise." %}

{% q "At the cleaning stop, three things about the record were changed by choices someone coded: how money is written, how IDs are written, which region got attached. None of those choices were wrong. So why do data teams insist that every one of them be written down and reviewable?" %}
Because a different reasonable choice produces a different number. Count the euro order at
yesterday's exchange rate instead of today's, or match IDs slightly differently, and "revenue"
shifts — with no bug anywhere. When two teams' numbers disagree (and they constantly do), the
explanation almost always lives in these invisible decisions, not in anyone's arithmetic.
Writing the choices down — in code, in documentation, in definitions everyone shares — is what
turns "my spreadsheet says something different" from a week-long argument into a five-minute
diff. A number you can trust is a number whose journey you can inspect.
{% endq %}

{% q "The manager's chart reads only the final summary table — it never touches the raw data. Give one reason that separation is deliberate, and one risk it creates." %}
**Why it's deliberate:** raw data is messy, huge, and changes shape; if every chart read it
directly, every chart would need its own cleaning logic, and they'd all disagree. Cleaning once,
in the middle, gives everyone the same answer — and keeps slow analytical queries away from the
systems running the actual business.

**The risk:** distance. Everyone downstream inherits whatever choices the cleaning steps made —
silently. If that logic is wrong, every chart built on it is wrong in the same convincing way,
and the person reading the dashboard has no way to see it. Trust concentrates in the middle of
the journey, which is exactly why that middle is where data teams put their tests.
{% endq %}

{% endcheck %}

{% section "The planes that didn't come back" %}

World War II. Bombers return from missions over Europe full of holes, and the military maps
every hit, hoping to armor the planes better. Armor is heavy — you can't protect everything. A
statistician named Abraham Wald was handed this data, and what he saw in it saved lives. In this
lesson, you get handed the same data. You have armor for two zones. Study the hit map and
choose.

{% activity "armor-allocation.html", "Armor allocation", "620px" %}

{% check "Think it through before you open the answers." %}

{% q "Every dot on the hit map was real — nobody made any measurement mistakes. So where, exactly, did the error live?" %}
In the population, not the measurements. The dataset was "hits on bombers that returned,"
quietly treated as "hits on bombers." The planes hit in the engines and cockpit mostly never
made it home to be measured — so the most important evidence was structurally missing from the
table, and no amount of careful analysis of the table could reveal that. This is why
professionals interrogate a dataset with a question that sounds almost paranoid: what would have
to happen for a record to end up in this data — and what kinds of records can never get in?
{% endq %}

{% q "Your company surveys its current customers and scores 9 out of 10 on satisfaction. Explain why this might be the bomber problem wearing a business suit. Who are the planes that didn't come back?" %}
The survey only reaches customers who are still around to answer it. The angriest customers
already canceled — they're the shot-down planes, invisible in the data precisely because of the
thing you're trying to measure. A 9/10 from survivors is perfectly consistent with a company
hemorrhaging unhappy customers. The fix mirrors Wald's: go looking for the missing population
(exit interviews, churned-customer outreach, comparing the surveyed group to the full customer
list) instead of squeezing more analysis out of the survivors. Once you know this pattern, you'll
see it everywhere: reviews come from people who didn't return the product, "success stories"
come from businesses that didn't fold, and workout advice comes from people the workout didn't
injure.
{% endq %}

{% endcheck %}

{% section "Almost right" %}

You will do data work with an AI assistant — nearly everyone in the field already does. And in
survey after survey, the same professionals who use AI daily name one frustration above all the
others: answers that are *almost* right. Not wrong in ways that jump out. Wrong in ways that
read smoothly, sound confident, and cost an afternoon when they slip through.

{% activity "review-queue.html", "Review queue", "660px" %}

{% check "Think it through before you open the answers." %}

{% q "The refund-rate mistake took you ten seconds to catch, because the table has 8 rows. At a real company it has 40 million rows and you can't eyeball anything. What could checking the AI's answer look like then?" %}
You stop checking the answer and start checking the method. Ask for the query and read it — does
it filter to refunded orders, or count something else? Compute the number a second, independent
way and see if the two agree. Sanity-check against what you already know: if last month's refund
rate was 24% and the AI says 12.5%, something changed — the business or the math. Spot-check a
sample by hand. Professionals also build these checks into the pipeline itself as automated
tests, so the checking happens every day, not just when someone gets suspicious. The reflex is
the same one you practiced here; only the tools scale up.
{% endq %}

{% q "Case 5 got the number right but invented a detail that wasn't in the data. Why is that arguably more dangerous than an answer that's plainly wrong?" %}
Because the true part buys trust for the false part. You verify the $70, feel done, and the
invented detail rides along into your report — where someone might act on it. Plainly wrong
answers get caught by the first person who looks; a fabrication attached to a verified fact can
survive several rounds of review, because each reviewer assumes checking part of the answer was
checking the answer. The lesson: verification doesn't transfer. Every claim needs its own
receipt — especially the ones sitting next to a claim that checked out.
{% endq %}

{% endcheck %}

## What's ahead

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
