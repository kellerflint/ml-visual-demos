/* ============================================================
   Site behaviour
   1. theme toggle (light / dark / follow system)
   2. provenance toggle — review scaffolding

   Activities are self-contained and set their own height via the
   {% activity %} shortcode. Nothing here touches them.
   ============================================================ */
(function () {
  "use strict";

  /* ---------- 1. theme ----------
     The no-flash inline script in <head> has already set data-theme.
     Here we only wire the button.                                   */
  var THEME_KEY = "aids-theme";

  function currentTheme() {
    var set = document.documentElement.getAttribute("data-theme");
    if (set) return set;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function initTheme() {
    var btn = document.getElementById("theme-toggle");
    if (!btn) return;
    btn.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      try { localStorage.setItem(THEME_KEY, next); } catch (e) {}
      btn.setAttribute("aria-label", next === "dark" ? "Switch to light mode" : "Switch to dark mode");
    });
  }

  /* ---------- 2. provenance ---------- */
  var PROV_KEY = "aids-prov";

  function initProv() {
    if (!document.querySelector(".prov")) return;

    var head = document.querySelector(".masthead .col");
    if (head && !document.getElementById("prov-legend")) {
      var lg = document.createElement("div");
      lg.id = "prov-legend";
      lg.innerHTML =
        '<span><strong>Where this came from:</strong></span>' +
        '<span class="swatch"><span class="dot" style="background:var(--prov-habiba)"></span><span class="lbl">Habiba</span></span>' +
        '<span class="swatch"><span class="dot" style="background:var(--prov-susan)"></span><span class="lbl">Susan</span></span>' +
        '<span class="swatch"><span class="dot" style="background:var(--prov-new)"></span><span class="lbl">New — wrapper</span></span>';
      head.appendChild(lg);
    }

    var btn = document.createElement("button");
    btn.id = "prov-toggle";
    btn.type = "button";
    document.body.appendChild(btn);

    function paint() {
      var off = document.body.classList.contains("prov-off");
      btn.textContent = off ? "◇ show sources" : "◆ hide sources";
      btn.setAttribute("aria-pressed", String(!off));
    }

    try {
      if (localStorage.getItem(PROV_KEY) === "off") document.body.classList.add("prov-off");
    } catch (e) {}

    btn.addEventListener("click", function () {
      var off = document.body.classList.toggle("prov-off");
      try { localStorage.setItem(PROV_KEY, off ? "off" : "on"); } catch (e) {}
      paint();
    });

    paint();
  }

  function init() { initTheme(); initProv(); }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
