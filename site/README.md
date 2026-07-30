# AI in Data Science — course site

Eleventy static site. Lesson prose is markdown; only the interactive activities are HTML.

```bash
npm install
npm run dev      # http://localhost:8080, live reload
npm run build    # → _site/
```

## Layout

```
src/
  index.md                  site home
  teaching-model.md         the design brief (shareable)
  _includes/
    base.njk                shell — head, theme toggle, masthead, footer
    lesson.njk              base + prev/next nav
  _data/site.json           site name, footer line
  assets/
    css/style.css           all styling, light + dark
    js/site.js              theme toggle · iframe auto-height · provenance toggle
  module-3/
    module-3.11tydata.json  sets layout for every page in the folder
    index.md                module landing
    01-…05-….md             the five lessons
    activities/*.html       self-contained, copied verbatim
```

## Writing a lesson

Frontmatter drives the masthead and the nav:

```yaml
---
order: 2
title: The eighth of April
kicker: Module 3 · Lesson 2 of 5
standfirst: One sentence under the title.
description: For <meta name="description">.
prev: { url: /module-3/01-what-counts-as-one/, label: "Lesson 1" }
next: { url: /module-3/03-who-is-missing/, label: "Lesson 3 · Who is missing?" }
---
```

Then write markdown, reaching for a shortcode only where the page needs structure.

## Shortcodes

Markdown works normally *inside* every paired shortcode — they run their content back
through markdown-it, so you don't have to drop into HTML.

| Shortcode | Use |
|---|---|
| `{% beat "01", "Cold open", "~3 min" %}` | Section divider for the six beats |
| `{% activity "six-phases.html", "The six phases", "600px" %}` | Embeds an activity with a header bar |
| `{% prov "habiba", "Habiba · scenario" %}…{% endprov %}` | Provenance block — `habiba`, `susan`, or `new` |
| `{% check "optional hint" %}…{% endcheck %}` | Check-yourself wrapper |
| `{% q "the question" %}…{% endq %}` | One reveal question, goes inside `check` |
| `{% callout %}…{% endcallout %}` | Aside. `{% callout "warn" %}` for the amber variant |
| `{% notebook "title", "colab-url" %}…{% endnotebook %}` | Notebook handoff + Colab button |
| `{% compare "optional label" %}…{% endcompare %}` | Wraps a markdown table in the comparison card |
| `{% instructor %}…{% endinstructor %}` | Facilitation notes panel |

## Activities

Self-contained HTML — inline CSS and JS, no external requests, no dependency on the page
embedding them. Each one is a real page at its own URL, so it can be opened directly, linked
to, or embedded by someone else in their own materials.

```
{% activity "six-phases.html", "The six phases", "600px" %}
```

renders a header bar whose **title is a link to the standalone file** (opens in a new tab),
a **Fullscreen** button, and the iframe at the height you give it. Fullscreen is an inline
handler on the button, so there is no page-level script wiring activities up — nothing in
`site.js` touches them.

Where they live:

- `src/activities/` for top-level pages → `/activities/<file>`
- `src/<section>/activities/` for pages inside a section → `/<section>/activities/<file>`

The shortcode picks the right one from the page URL. Activities are added to
`eleventyConfig.ignores` so the template engine never parses them, then passed through
verbatim — their inline JS is not Nunjucks and must not be treated as such.

Activities stay light in dark mode by design. The embed's header and border frame them so
they read as a panel rather than a glare.

Set the height to fit the content. There is no auto-height; a fixed height keeps the embed
predictable, and anything taller than it needs can be opened fullscreen or in its own tab.

## Dark mode

Every colour is a CSS variable. `:root` holds the light values; the dark values appear
twice — once under `@media (prefers-color-scheme: dark)` for people who never touch the
toggle, once under `:root[data-theme="dark"]` for people who do. An inline script in
`base.njk` applies the stored preference before first paint, so there is no flash.

Anything new should use the variables rather than literal colours, and it will theme itself.

## Provenance markers

`{% prov %}` blocks are review scaffolding, not part of the finished course — they show
whether a passage came from Habiba, from Susan, or is new. The "hide sources" button
bottom-right turns them off, and the preference persists across pages.

To strip them for production: delete the `.prov` rules from `style.css` and the
`initProv()` call in `site.js`. The blocks degrade to plain `<div>`s.
