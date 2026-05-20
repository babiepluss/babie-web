document.documentElement.classList.add("js");

const navToggle = document.querySelector("[data-nav-toggle]");
const siteNav = document.querySelector("#site-nav");

if (navToggle && siteNav) {
  navToggle.hidden = false;

  const setMenu = (isOpen) => {
    navToggle.setAttribute("aria-expanded", String(isOpen));
    navToggle.setAttribute("aria-label", isOpen ? "Menüyü kapat" : "Menüyü aç");
    siteNav.classList.toggle("is-open", isOpen);
    document.body.classList.toggle("nav-open", isOpen);
    window.dispatchEvent(new Event("sticky-cta-check"));
  };

  navToggle.addEventListener("click", () => {
    setMenu(navToggle.getAttribute("aria-expanded") !== "true");
  });

  siteNav.addEventListener("click", (event) => {
    if (event.target instanceof HTMLAnchorElement) {
      setMenu(false);
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      setMenu(false);
    }
  });
}

const stickyCta = document.querySelector(".sticky-cta");

if (stickyCta) {
  const contactSection = document.querySelector(".contact-section");
  const siteFooter = document.querySelector(".site-footer");
  const heroSection = document.querySelector(".hero");
  const heroActions = document.querySelector(".hero-actions");
  const smallViewportQuery = window.matchMedia("(max-width: 620px)");

  const shouldShowStickyCta = () => {
    if (!smallViewportQuery.matches) return false;
    if (document.body.classList.contains("nav-open")) return false;

    const scrollY = window.scrollY;
    const heroBottom = heroActions
      ? (heroSection ?? heroActions).getBoundingClientRect().bottom + scrollY
      : Math.min(520, window.innerHeight * 0.62);
    if (scrollY <= heroBottom) return false;

    if (contactSection) {
      const rect = contactSection.getBoundingClientRect();
      if (rect.top < window.innerHeight && rect.bottom > 0) return false;
    }

    if (siteFooter) {
      const rect = siteFooter.getBoundingClientRect();
      if (rect.top < window.innerHeight) return false;
    }

    return true;
  };

  const updateStickyCta = () => {
    stickyCta.classList.toggle("is-visible", shouldShowStickyCta());
  };

  updateStickyCta();
  window.addEventListener("scroll", updateStickyCta, { passive: true });
  window.addEventListener("resize", updateStickyCta);
  window.addEventListener("sticky-cta-check", updateStickyCta);
}

const revealItems = document.querySelectorAll(".reveal");

if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.16 }
  );

  revealItems.forEach((item) => observer.observe(item));
} else {
  revealItems.forEach((item) => item.classList.add("is-visible"));
}

// --- Recommendation studio (separate page, phase-driven) -----------------

const studio = document.querySelector("[data-studio]");

if (studio) {
  // Hydrate phase visibility now that JS is available.
  // Server renders all phases visible (so no-JS users see the questions).
  // Once JS loads, we hide phases marked data-studio-initial-hidden="true",
  // and hide all step fieldsets except the first.
  studio.querySelectorAll('[data-studio-initial-hidden="true"]').forEach((node) => {
    node.hidden = true;
  });
  studio.querySelectorAll('[data-studio-step-initial-hidden="true"]').forEach((node) => {
    node.hidden = true;
  });

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const phases = {
    intro: studio.querySelector('[data-phase="intro"]'),
    questions: studio.querySelector('[data-phase="questions"]'),
    transition: studio.querySelector('[data-phase="transition"]'),
    result: studio.querySelector('[data-phase="result"]'),
  };
  const railSteps = Array.from(studio.querySelectorAll("[data-rail-phase]"));
  const startBtn = studio.querySelector("[data-studio-start]");
  const form = phases.questions;
  const stepNodes = Array.from(form.querySelectorAll("[data-studio-step]"));
  const totalSteps = stepNodes.length;
  const progressCurrentEl = studio.querySelector("[data-progress-current]");
  const progressFill = studio.querySelector("[data-progress-fill]");
  const transitionItems = Array.from(
    studio.querySelectorAll("[data-transition-step]")
  );

  const result = phases.result;
  const nameEl = result.querySelector("[data-studio-name]");
  const summaryEl = result.querySelector("[data-studio-summary]");
  const layersEl = result.querySelector("[data-studio-layers]");
  const rationaleEl = result.querySelector("[data-studio-rationale]");
  const choicesEl = result.querySelector("[data-studio-choices]");
  const restartBtn = result.querySelector("[data-studio-restart]");
  const editBtn = result.querySelector("[data-studio-edit]");

  let currentStep = 0; // 0..totalSteps-1
  let phase = "intro";
  let transitionTimer = null;
  let revealTimer = null;

  // -------- Recommendation content maps (deterministic, truth-safe) -------

  const PACKAGE_NAME = {
    starter: "Sade Başlangıç Çerçevesi",
    daily: "Günlük Akış Kolaylığı",
    balance: "Hassas Denge Paketi",
    gift: "Yeni Dönem Hediye Seçkisi",
  };

  const AGE_LAYER = {
    "0-3": { label: "Yenidoğan dönemi", text: "İlk haftalarda sade ve sık tekrarlayan ihtiyaç odağı." },
    "4-6": { label: "Erken bakım dönemi", text: "Cilt ve hijyen rutinine yumuşak bir geçiş katmanı." },
    "7-9": { label: "Hareketli keşif dönemi", text: "Daha aktif gün ritmine uygun pratik bir akış." },
    "10-12": { label: "İlk yaş eşiği", text: "Tekstil ve günlük kullanım dengesini gözeten katman." },
    "13-18": { label: "Yürüme dönemi", text: "Dışarıda dayanıklı ve pratik bir bakım odağı." },
    "19-24": { label: "İkinci yaş yaklaşımı", text: "Gelişen rutine uygun düzenli tekrar mantığı." },
  };

  const NEED_LAYER = {
    daily: { label: "Temel hijyen odağı", text: "Bez, mendil ve günlük temizlik akışı." },
    skin: { label: "Hassas cilt katmanı", text: "Yumuşak içerikli bakım ürünü fikri." },
    outdoor: { label: "Pratik kullanım katmanı", text: "Dışarıda taşınması kolay temel ihtiyaç akışı." },
    gift: { label: "Hediye sunumu katmanı", text: "Yeni başlangıç için derli toplu bir seçki." },
    routine: { label: "Tekrar düzeni katmanı", text: "Düzenli ihtiyaçların sakin takibi." },
  };

  const SENSITIVITY_LAYER = {
    scent: { label: "Koku filtresi", text: "Düşük kokulu ürün tercihi öne çıkarılır." },
    ingredient: { label: "İçerik filtresi", text: "Hassas içerik notu öne çıkarılır." },
    fabric: { label: "Doku filtresi", text: "Ekstra yumuşak tekstil ve mendil önceliği." },
    none: { label: "Genel denge", text: "Şimdilik özel bir filtre uygulanmaz." },
  };

  const TONE_LAYER = {
    starter: { label: "Sade kapanış", text: "Az ama yeterli, başlangıç hissi veren paket." },
    daily: { label: "Günlük rahatlık", text: "Tekrar eden ihtiyaçlara odaklı yumuşak akış." },
    balance: { label: "Hassas denge", text: "Bakım ve hijyen arasında yumuşak denge." },
    gift: { label: "Hediye sunumu", text: "Yeni dönem için hoş, derli toplu bir kapanış." },
  };

  const AGE_SUMMARY = {
    "0-3": "Yenidoğan döneminde sade tekrar önemli bir rahatlık sağlar",
    "4-6": "Bu dönemde ihtiyaçlar çeşitlenir; sakin bir ritim yardımcı olur",
    "7-9": "Hareketin arttığı bu dönemde pratik bir akış öne çıkar",
    "10-12": "İlk yaş yaklaşırken tekstil ve günlük kullanım daha belirleyici olur",
    "13-18": "Yürüme döneminde dışarıyla uyumlu pratik dokunuşlar değer kazanır",
    "19-24": "İkinci yaş öncesi düzen ve tekrar mantığı belirgin bir rahatlık verir",
  };

  const NEED_PHRASE = {
    daily: "günlük temel ihtiyaçlara",
    skin: "hassas cilt önceliğine",
    outdoor: "dışarıda pratik kullanıma",
    gift: "hediye sunumu odağına",
    routine: "düzenli tekrar kolaylığına",
  };

  const SENSITIVITY_PHRASE_OPEN = {
    scent: "Koku hassasiyetini gözeten",
    ingredient: "İçerik hassasiyetini gözeten",
    fabric: "Yumuşak doku tercihini öne çıkaran",
    none: "Belirli bir filtre olmadan ilerleyen",
  };

  const SENSITIVITY_PHRASE_TAIL = {
    scent: "düşük kokulu seçimlerle",
    ingredient: "hassas içerik notlarıyla",
    fabric: "yumuşak doku tercihiyle",
    none: "genel bir denge gözeterek",
  };

  const TONE_PHRASE = {
    starter: "sade bir başlangıç hissiyle kapanır",
    daily: "günlük rahatlık tonunda kapanır",
    balance: "hassas bakım dengesiyle kapanır",
    gift: "hediye sunumu tonunda kapanır",
  };

  // Friendly choice labels for the "choices summary" chip list.
  const STEP_LABELS = {
    age: "Dönem",
    need: "İhtiyaç",
    sensitivity: "Hassasiyet",
    tone: "Ton",
  };

  const OPTION_LABEL = {
    age: {
      "0-3": "0-3 ay",
      "4-6": "4-6 ay",
      "7-9": "7-9 ay",
      "10-12": "10-12 ay",
      "13-18": "13-18 ay",
      "19-24": "19-24 ay",
    },
    need: {
      daily: "Günlük temel ihtiyaç",
      skin: "Hassas cilt odağı",
      outdoor: "Dışarıda pratik kullanım",
      gift: "Hediye / yeni başlangıç",
      routine: "Düzenli tekrar kolaylığı",
    },
    sensitivity: {
      scent: "Koku hassasiyeti",
      ingredient: "İçerik hassasiyeti",
      fabric: "Ekstra yumuşak doku",
      none: "Şimdilik özel not yok",
    },
    tone: {
      starter: "Sade başlangıç",
      daily: "Günlük rahatlık",
      balance: "Hassas bakım dengesi",
      gift: "Hediye gibi seçki",
    },
  };

  const SNAPSHOT_STORAGE_KEY = "babie:studio-snapshot";

  // -------- Helpers ----------------------------------------------------------

  const buildSummary = (choice) => {
    const ageLine = AGE_SUMMARY[choice.age];
    const needLine = NEED_PHRASE[choice.need];
    return `${ageLine}. Bu çerçeve, ${needLine} odaklanır ve ${TONE_PHRASE[choice.tone]}.`;
  };

  const buildRationale = (choice) => {
    const opener = SENSITIVITY_PHRASE_OPEN[choice.sensitivity];
    const tail = SENSITIVITY_PHRASE_TAIL[choice.sensitivity];
    const needLine = NEED_PHRASE[choice.need];
    const packageName = PACKAGE_NAME[choice.tone] ?? PACKAGE_NAME.daily;
    return `${opener} bu yaklaşım, ${choice.age} ay aralığında ${needLine} öncelik veren ve ${tail} ilerleyen "${packageName}" çerçevesini öne çıkarır.`;
  };

  const buildLayers = (choice) => [
    AGE_LAYER[choice.age],
    NEED_LAYER[choice.need],
    SENSITIVITY_LAYER[choice.sensitivity],
    TONE_LAYER[choice.tone],
  ];

  const readChoice = () => {
    const data = new FormData(form);
    return {
      age: data.get("studio-age") ?? "4-6",
      need: data.get("studio-need") ?? "daily",
      sensitivity: data.get("studio-sensitivity") ?? "none",
      tone: data.get("studio-tone") ?? "daily",
    };
  };

  const renderLayers = (layers) => {
    layersEl.innerHTML = "";
    layers.forEach((layer, i) => {
      const wrap = document.createElement("div");
      wrap.className = "studio-layer";

      const idx = document.createElement("span");
      idx.className = "micro-label";
      idx.textContent = "0" + (i + 1);

      const body = document.createElement("div");
      const h4 = document.createElement("h4");
      h4.textContent = layer.label;
      const p = document.createElement("p");
      p.textContent = layer.text;
      body.append(h4, p);

      wrap.append(idx, body);
      layersEl.append(wrap);
    });
  };

  const renderChoices = (choice) => {
    if (!choicesEl) return;
    choicesEl.innerHTML = "";
    Object.entries(STEP_LABELS).forEach(([key, friendlyKey]) => {
      const li = document.createElement("li");
      li.className = "studio-choice";

      const k = document.createElement("span");
      k.className = "studio-choice-key";
      k.textContent = friendlyKey;

      const v = document.createElement("span");
      v.className = "studio-choice-value";
      v.textContent = OPTION_LABEL[key]?.[choice[key]] ?? "—";

      li.append(k, v);
      choicesEl.append(li);
    });
  };

  const renderResult = () => {
    const choice = readChoice();
    const layers = buildLayers(choice);

    const packageName = PACKAGE_NAME[choice.tone] ?? PACKAGE_NAME.daily;
    nameEl.textContent = packageName;
    summaryEl.textContent = buildSummary(choice);
    renderLayers(layers);
    rationaleEl.textContent = buildRationale(choice);
    renderChoices(choice);

    // Persist a small snapshot for the plan comparison page to hydrate from.
    persistSnapshot({
      choice,
      packageName,
      summary: buildSummary(choice),
    });
  };

  const persistSnapshot = (snapshot) => {
    try {
      const payload = {
        ...snapshot,
        savedAt: Date.now(),
      };
      sessionStorage.setItem(SNAPSHOT_STORAGE_KEY, JSON.stringify(payload));
    } catch (_err) {
      // sessionStorage may be disabled (e.g. private mode); fail silently.
    }
  };

  const clearSnapshot = () => {
    try {
      sessionStorage.removeItem(SNAPSHOT_STORAGE_KEY);
    } catch (_err) {
      // sessionStorage may be disabled (e.g. private mode); fail silently.
    }
  };

  // -------- Phase rail ------------------------------------------------------

  const setRail = (activePhase, opts = {}) => {
    const completed = opts.completed ?? false;
    let seenCurrent = false;
    railSteps.forEach((node) => {
      const railPhase = node.dataset.railPhase;
      node.classList.remove("is-current", "is-complete");
      node.removeAttribute("aria-current");

      if (railPhase === activePhase) {
        node.classList.add("is-current");
        node.setAttribute("aria-current", "step");
        seenCurrent = true;
      } else if (!seenCurrent) {
        node.classList.add("is-complete");
      }
    });
    if (completed) {
      railSteps.forEach((node) => {
        node.classList.remove("is-current");
        node.classList.add("is-complete");
        node.removeAttribute("aria-current");
      });
    }
  };

  // -------- Step navigation -------------------------------------------------

  const updateProgressReadout = () => {
    if (progressCurrentEl) {
      progressCurrentEl.textContent = String(currentStep + 1);
    }
    if (progressFill) {
      const pct = ((currentStep + 1) / totalSteps) * 100;
      progressFill.style.width = `${pct}%`;
    }
  };

  const showStepNode = (i, { focus = true } = {}) => {
    stepNodes.forEach((node, idx) => {
      const visible = idx === i;
      node.hidden = !visible;
      node.classList.toggle("is-active", visible);
    });
    currentStep = i;
    updateProgressReadout();

    if (focus) {
      const active = stepNodes[i];
      const target =
        active.querySelector("input[type=radio]:checked") ??
        active.querySelector("input[type=radio]") ??
        active;
      target?.focus({ preventScroll: false });
    }
  };

  // -------- Phase orchestration ---------------------------------------------

  const setPhase = (next, opts = {}) => {
    phase = next;
    studio.dataset.studioPhase = next;

    Object.entries(phases).forEach(([key, node]) => {
      if (!node) return;
      const visible = key === next;
      node.hidden = !visible;
      node.classList.toggle("is-active", visible);
    });

    if (next === "result") {
      setRail("result", { completed: true });
    } else {
      setRail(next);
    }

    if (next === "questions") {
      const stepIndex = opts.stepIndex ?? 0;
      showStepNode(stepIndex, { focus: opts.focus !== false });
    }

    if (next === "transition") {
      runTransition();
    }

    if (next === "result") {
      renderResult();
      // Move focus to result heading once revealed.
      requestAnimationFrame(() => {
        result.focus({ preventScroll: false });
      });
    }

    if (next === "intro" && opts.focus !== false) {
      startBtn?.focus({ preventScroll: false });
    }
  };

  // -------- Transition runner -----------------------------------------------

  const runTransition = () => {
    if (transitionTimer) {
      clearTimeout(transitionTimer);
      transitionTimer = null;
    }
    if (revealTimer) {
      clearTimeout(revealTimer);
      revealTimer = null;
    }

    transitionItems.forEach((item) => item.classList.remove("is-active"));

    if (reduceMotion) {
      // Show everything immediately, then move on.
      transitionItems.forEach((item) => item.classList.add("is-active"));
      revealTimer = setTimeout(() => setPhase("result"), 240);
      return;
    }

    const stagger = 380;
    transitionItems.forEach((item, i) => {
      setTimeout(() => item.classList.add("is-active"), 80 + i * stagger);
    });
    const total = 80 + transitionItems.length * stagger + 280;
    revealTimer = setTimeout(() => setPhase("result"), total);
  };

  // -------- Wiring up controls ----------------------------------------------

  startBtn?.addEventListener("click", () => {
    setPhase("questions", { stepIndex: 0 });
  });

  // Wire up next/back buttons inside each step.
  stepNodes.forEach((node, i) => {
    const nextBtn = node.querySelector("[data-studio-next]");
    const backBtn = node.querySelector("[data-studio-back]");
    const backToIntroBtn = node.querySelector("[data-studio-back-to-intro]");

    nextBtn?.addEventListener("click", () => {
      if (i === totalSteps - 1) {
        setPhase("transition");
      } else {
        showStepNode(i + 1);
      }
    });

    backBtn?.addEventListener("click", () => {
      if (i === 0) {
        setPhase("intro");
      } else {
        showStepNode(i - 1);
      }
    });

    backToIntroBtn?.addEventListener("click", () => {
      setPhase("intro");
    });
  });

  restartBtn?.addEventListener("click", () => {
    clearSnapshot();
    form.reset();
    showStepNode(0, { focus: false });
    setPhase("intro");
  });

  editBtn?.addEventListener("click", () => {
    setPhase("questions", { stepIndex: 0 });
  });

  // Initial state: render intro phase, do not steal focus on page load.
  setPhase("intro", { focus: false });
}


// --- Plan comparison surface ---------------------------------------------

const access = document.querySelector("[data-access]");

if (access) {
  const detailsScript = document.querySelector("[data-access-plan-details]");
  const planMapScript = document.querySelector("[data-access-plan-map]");
  let planDetails = {};
  let planMap = {};

  try {
    planDetails = detailsScript ? JSON.parse(detailsScript.textContent) : {};
  } catch (_e) {
    planDetails = {};
  }
  try {
    planMap = planMapScript ? JSON.parse(planMapScript.textContent) : {};
  } catch (_e) {
    planMap = {};
  }

  const cards = Array.from(access.querySelectorAll("[data-access-card]"));
  const detailEyebrow = access.querySelector("[data-access-detail-eyebrow]");
  const detailTitle = access.querySelector("[data-access-detail-title]");
  const detailBody = access.querySelector("[data-access-detail-body]");
  const detailPoints = access.querySelector("[data-access-detail-points]");

  const contextNode = access.querySelector("[data-access-context]");
  const contextEyebrow = access.querySelector("[data-access-context-eyebrow]");
  const contextName = access.querySelector("[data-access-context-name]");
  const contextSummary = access.querySelector("[data-access-context-summary]");
  const contextFit = access.querySelector("[data-access-context-fit]");
  const contextDefault = access.querySelector("[data-access-context-default]");

  const defaultPlan = access.dataset.defaultPlan || "plus";

  const renderList = (node, items) => {
    if (!node) return;
    node.innerHTML = "";
    items.forEach((text) => {
      const li = document.createElement("li");
      li.textContent = text;
      node.append(li);
    });
  };

  const renderDetail = (planKey) => {
    const detail = planDetails[planKey];
    if (!detail) return;
    if (detailEyebrow) detailEyebrow.textContent = detail.eyebrow;
    if (detailTitle) detailTitle.textContent = detail.title;
    if (detailBody) detailBody.textContent = detail.body;
    renderList(detailPoints, detail.points ?? []);
  };

  const setSelected = (planKey, { focus = false } = {}) => {
    cards.forEach((card) => {
      const isSelected = card.dataset.plan === planKey;
      const cta = card.querySelector("[data-access-card-cta]");
      const selectedBadge = card.querySelector("[data-access-selected-badge]");
      card.classList.toggle("is-selected", isSelected);
      cta?.setAttribute("aria-pressed", String(isSelected));
      if (cta) {
        cta.textContent = isSelected
          ? cta.dataset.labelSelected || "Seçili plan"
          : cta.dataset.labelDefault || "Planı incele";
      }
      if (selectedBadge) {
        selectedBadge.hidden = !isSelected;
      }
      if (isSelected && focus) {
        card.scrollIntoView({ block: "nearest", behavior: "smooth" });
      }
    });
    renderDetail(planKey);
  };

  const setRecommended = (planKey) => {
    cards.forEach((card) => {
      const badge = card.querySelector("[data-access-recommended]");
      if (!badge) return;
      const isMatch = card.dataset.plan === planKey;
      badge.hidden = !isMatch;
      card.classList.toggle("is-recommended", isMatch);
    });
  };

  // Hydrate context ribbon from sessionStorage if a snapshot exists.
  let snapshot = null;
  try {
    const raw = sessionStorage.getItem("babie:studio-snapshot");
    if (raw) snapshot = JSON.parse(raw);
  } catch (_e) {
    snapshot = null;
  }

  let initialPlan = defaultPlan;

  if (snapshot && snapshot.choice) {
    const tone = snapshot.choice.tone;
    const recommendedPlan = planMap[tone] || defaultPlan;
    const recommendedCard = cards.find((card) => card.dataset.plan === recommendedPlan);

    if (contextNode) contextNode.hidden = false;
    if (contextDefault) contextDefault.hidden = true;
    if (contextName) {
      contextName.textContent = snapshot.packageName || contextName.textContent || "Stüdyo önerisi";
    }
    if (contextSummary && snapshot.summary) {
      contextSummary.textContent = snapshot.summary;
    }

    // Friendly fit line.
    const planName =
      recommendedCard?.querySelector(".access-card-name")?.textContent || "";
    if (contextFit && planName) {
      contextFit.textContent = `Seçimlerinize göre "${planName}" planı size daha yakın görünüyor.`;
    }

    setRecommended(recommendedPlan);
    initialPlan = recommendedPlan;
  } else {
    if (contextNode) contextNode.hidden = true;
    if (contextDefault) contextDefault.hidden = false;
  }

  // Wire up the CTA buttons as the only selection controls.
  cards.forEach((card) => {
    const cta = card.querySelector("[data-access-card-cta]");
    const select = () => setSelected(card.dataset.plan, { focus: true });
    cta?.addEventListener("click", (event) => {
      event.stopPropagation();
      select();
    });
  });

  // Initial detail render based on default or recommended plan.
  setSelected(initialPlan);
}
