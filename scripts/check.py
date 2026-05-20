import os
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"


def normalize_base_path(raw_base_path: str | None) -> str:
    if raw_base_path is None:
        return "/"

    base_path = raw_base_path.strip()
    if not base_path or base_path == "/":
        return "/"
    if "://" in base_path:
        fail("BABIE_SITE_BASE_PATH must be a path, not a full URL")

    return "/" + base_path.strip("/") + "/"


SITE_BASE_PATH = normalize_base_path(os.getenv("BABIE_SITE_BASE_PATH"))
HOME_PATH = SITE_BASE_PATH
RECOMMENDATION_PATH = f"{SITE_BASE_PATH}oneri/"
EARLY_ACCESS_PATH = f"{SITE_BASE_PATH}erken-erisim/"

REQUIRED_FILES = [
    DIST / "index.html",
    DIST / "oneri" / "index.html",
    DIST / "erken-erisim" / "index.html",
    DIST / "assets" / "styles.css",
    DIST / "assets" / "app.js",
    DIST / ".nojekyll",
]

REQUIRED_HOME_IDS = {
    "hero",
    "problemler",
    "nasil-calisir",
    "kutu-mantigi",
    "guven",
    "sss",
    "iletisim",
}

FORBIDDEN_COPY = [
    "doktor onaylı",
    "pediatrist onaylı",
    "pediatrist önerdi",
    "pediatrist onayladı",
    "aktif abonelik",
    "aktif hizmet",
    "canlı topluluk",
    "tam çalışan yapay zeka",
    "yapay zeka karar motoru",
    "ai sizin için karar",
    "akıllı motor",
    "ai analiz ediyor",
    "ai takip ediyor",
    "kusursuz",
    "teslimat garantisi",
    "teslimat tarihi",
    "kargoya verildi",
    "sepete ekle",
    "ödeme yap",
    "ödeme adımına geç",
    "ödeme yapın",
    "satın alın",
    "sipariş ver",
    "siparişi tamamla",
    "premium'u yükselt",
    "premium'u seçin",
    "planı satın al",
    "aboneliği aç",
    "aboneliğin başladı",
    "aboneliğiniz başladı",
    "üyeliğin aktif",
    "üyeliğiniz aktif",
    "stoklarla sınırlı",
    "tüm türkiye'de aktif",
]

class AuditParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.landmarks: list[str] = []
        self.elements: list[tuple[str, dict[str, str | None]]] = []
        self.anchors: list[dict[str, str | None]] = []
        self.buttons: list[dict[str, str | None]] = []
        self.forms: list[dict[str, str | None]] = []
        self.labels: list[dict[str, str | None]] = []
        self.controls: list[tuple[str, dict[str, str | None]]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = dict(attrs)
        self.elements.append((tag, attr_map))
        if "id" in attr_map and attr_map["id"]:
            self.ids.add(attr_map["id"])
        if tag in {"header", "main", "footer", "nav", "section"}:
            self.landmarks.append(tag)
        if tag == "a":
            self.anchors.append(attr_map)
        if tag == "button":
            self.buttons.append(attr_map)
        if tag == "form":
            self.forms.append(attr_map)
        if tag == "label":
            self.labels.append(attr_map)
        if tag in {"input", "select", "textarea"}:
            self.controls.append((tag, attr_map))


def fail(message: str) -> None:
    print(f"Check failed: {message}")
    sys.exit(1)


def parse(html: str) -> AuditParser:
    p = AuditParser()
    p.feed(html)
    return p


def css_rules(css: str) -> list[tuple[str, dict[str, str]]]:
    css_without_comments = re.sub(r"/\*.*?\*/", "", css, flags=re.DOTALL)
    rules: list[tuple[str, dict[str, str]]] = []

    for match in re.finditer(r"([^{}]+)\{([^{}]*)\}", css_without_comments):
        selectors = [selector.strip() for selector in match.group(1).split(",")]
        declarations: dict[str, str] = {}
        for declaration in match.group(2).split(";"):
            if ":" not in declaration:
                continue
            property_name, value = declaration.split(":", 1)
            declarations[property_name.strip().casefold()] = value.strip().casefold()

        for selector in selectors:
            if selector:
                rules.append((selector, declarations))

    return rules


def rules_for_selector(rules: list[tuple[str, dict[str, str]]], selector: str) -> list[dict[str, str]]:
    return [declarations for rule_selector, declarations in rules if rule_selector == selector]


def assert_home_page(html: str) -> None:
    parser = parse(html)

    missing_ids = REQUIRED_HOME_IDS.difference(parser.ids)
    if missing_ids:
        fail(f"home page missing section ids: {', '.join(sorted(missing_ids))}")

    for landmark in ("header", "main", "footer", "nav"):
        if landmark not in parser.landmarks:
            fail(f"home page missing semantic landmark: {landmark}")

    nav_toggle = [b for b in parser.buttons if b.get("aria-controls") == "site-nav"]
    if not nav_toggle or nav_toggle[0].get("aria-expanded") is None:
        fail("home page mobile nav toggle needs aria-controls and aria-expanded")
    if "hidden" not in nav_toggle[0]:
        fail("home page mobile nav toggle must be hidden before JS enables it")

    # Home page must NOT contain a recommendation studio (form with radio inputs).
    studio_radios = [
        attrs
        for tag, attrs in parser.controls
        if tag == "input" and (attrs.get("type") or "").casefold() == "radio"
    ]
    if studio_radios:
        fail("home page must not embed the recommendation studio form (no radio inputs)")

    # Home page must not include the studio aria-live result panel.
    if "data-studio-result" in html:
        fail("home page must not embed the studio result panel")

    # Header CTA, hero primary CTA and sticky CTA should target the recommendation page.
    sticky = [a for a in parser.anchors if "sticky-cta" in (a.get("class") or "")]
    if not sticky:
        fail("home page must keep the sticky CTA hook")
    if sticky[0].get("href") != RECOMMENDATION_PATH:
        fail(
            "home page sticky CTA must point to "
            f"{RECOMMENDATION_PATH} (got {sticky[0].get('href')})"
        )

    header_cta = [a for a in parser.anchors if "header-cta" in (a.get("class") or "")]
    if not header_cta:
        fail("home page must keep the header CTA")
    if header_cta[0].get("href") != RECOMMENDATION_PATH:
        fail(
            "home page header CTA must point to "
            f"{RECOMMENDATION_PATH} (got {header_cta[0].get('href')})"
        )

    # Hero primary CTA points to the recommendation page.
    hero_primary = next(
        (
            a
            for a in parser.anchors
            if "button-primary" in (a.get("class") or "")
            and a.get("href", "").startswith(RECOMMENDATION_PATH)
        ),
        None,
    )
    if hero_primary is None:
        fail("home page must include a primary CTA pointing to the recommendation page")

    instagram_href = "https://www.instagram.com/babieplus/?utm_source=ig_web_button_share_sheet"
    instagram_link = next(
        (
            a
            for a in parser.anchors
            if "contact-card" in (a.get("class") or "")
            and a.get("href") == instagram_href
        ),
        None,
    )
    if instagram_link is None:
        fail("home page contact section must include the Babie+ Instagram link")
    if instagram_link.get("target") != "_blank" or "noopener" not in (instagram_link.get("rel") or ""):
        fail("external Instagram contact link must open safely with target _blank + noopener")

    mail_link = next(
        (
            a
            for a in parser.anchors
            if "contact-card" in (a.get("class") or "")
            and a.get("href") == "mailto:babieplus@gmail.com"
        ),
        None,
    )
    if mail_link is None:
        fail("home page contact section must include the Babie+ e-mail link")


def assert_recommendation_page(html: str) -> None:
    parser = parse(html)

    for landmark in ("header", "main", "footer", "nav"):
        if landmark not in parser.landmarks:
            fail(f"recommendation page missing semantic landmark: {landmark}")

    forms = [
        attrs
        for tag, attrs in parser.elements
        if tag == "form" and "data-studio-form" in attrs
    ]
    if len(forms) != 1:
        fail("recommendation page needs exactly one data-studio-form")

    form = forms[0]
    onsubmit = (form.get("onsubmit") or "").replace(" ", "").casefold()
    if "returnfalse" not in onsubmit:
        fail("studio form must block submit with onsubmit=\"return false;\"")
    if form.get("action") or form.get("method"):
        fail("studio form must not declare action or method (no backend submit)")

    # No submit-capable buttons.
    for attrs in parser.buttons:
        button_type = (attrs.get("type") or "submit").casefold()
        if button_type == "submit":
            fail("studio must not expose submit-capable buttons")

    # Only radio inputs allowed.
    for tag, attrs in parser.controls:
        if tag in {"select", "textarea"}:
            fail(f"studio must not expose <{tag}> controls")
        if tag == "input":
            input_type = (attrs.get("type") or "text").casefold()
            if input_type != "radio":
                fail(f"studio must only use radio inputs, found type={input_type}")

    # Each radio input must have a matching <label for>.
    labels_for = {attrs.get("for") for attrs in parser.labels if attrs.get("for")}
    radio_ids = {
        attrs.get("id")
        for tag, attrs in parser.controls
        if tag == "input"
        and (attrs.get("type") or "").casefold() == "radio"
        and attrs.get("id")
    }
    missing_labels = radio_ids.difference(labels_for)
    if missing_labels:
        fail(
            "studio radio inputs missing label associations: "
            f"{', '.join(sorted(missing_labels))}"
        )
    if not radio_ids:
        fail("studio must expose at least one radio input")

    # Phase orchestration hooks.
    studio_root = [attrs for _, attrs in parser.elements if "data-studio" in attrs]
    if len(studio_root) != 1:
        fail("recommendation page needs exactly one data-studio root")
    if (studio_root[0].get("data-studio-phase") or "") != "intro":
        fail("studio root must start in the intro phase (data-studio-phase=\"intro\")")

    phase_attrs = [
        attrs.get("data-phase")
        for _, attrs in parser.elements
        if "data-phase" in attrs and attrs.get("data-phase")
    ]
    expected_phases = {"intro", "questions", "transition", "result"}
    if set(phase_attrs) != expected_phases:
        fail(
            "recommendation page must declare all four phases: intro, questions, "
            f"transition, result (found: {sorted(set(phase_attrs))})"
        )

    # Intro phase needs a start button hook.
    if not any("data-studio-start" in attrs for attrs in parser.buttons):
        fail("intro phase must expose a data-studio-start button")

    # Transition phase needs aria-live polite (we look at any element).
    transition_nodes = [
        attrs
        for _, attrs in parser.elements
        if attrs.get("data-phase") == "transition"
    ]
    if (transition_nodes[0].get("aria-live") or "").casefold() != "polite":
        fail("transition phase must be aria-live=\"polite\"")

    # Result panel hooks.
    result_nodes = [
        attrs for _, attrs in parser.elements if "data-studio-result" in attrs
    ]
    if len(result_nodes) != 1:
        fail("recommendation page needs exactly one data-studio-result panel")
    if (result_nodes[0].get("aria-live") or "").casefold() != "polite":
        fail("studio result panel must be aria-live=\"polite\"")
    if result_nodes[0].get("tabindex") != "-1":
        fail("studio result panel must be focusable via tabindex=\"-1\"")

    # Step navigation hooks present.
    if not any("data-studio-next" in attrs for attrs in parser.buttons):
        fail("studio must expose at least one data-studio-next button")
    if not any("data-studio-back" in attrs for attrs in parser.buttons):
        fail("studio must expose a back button on subsequent steps")
    if not any("data-studio-back-to-intro" in attrs for attrs in parser.buttons):
        fail("studio must expose a visible back-to-intro control on step 1")

    # Result panel must offer edit + restart hooks.
    if not any("data-studio-edit" in attrs for attrs in parser.buttons):
        fail("result panel must expose a data-studio-edit button")
    if not any("data-studio-restart" in attrs for attrs in parser.buttons):
        fail("result panel must expose a data-studio-restart button")

    # Result panel primary CTA must point to the plan comparison page (not FAQ).
    primary_anchors = [
        a
        for a in parser.anchors
        if "studio-next-primary" in (a.get("class") or "")
    ]
    if not primary_anchors:
        fail("result panel must include a primary CTA into the plan comparison page")
    if primary_anchors[0].get("href") != EARLY_ACCESS_PATH:
        fail(
            "result panel primary CTA must point to "
            f"{EARLY_ACCESS_PATH} (got {primary_anchors[0].get('href')})"
        )

    # No forbidden marketplace language inside the studio surface.
    body_text = re.sub(r"<[^>]+>", " ", html).casefold()
    forbidden_local = [
        "sepete ekle",
        "satın alın",
        "siparişi tamamla",
        "ücretsiz kargo",
        "stoklarla sınırlı",
        "ödeme adımına geç",
        "ödeme yapın",
        "aboneliğiniz başladı",
        "teslimat tarihi",
        "kargoya verildi",
        "pediatrist onayladı",
    ]
    for phrase in forbidden_local:
        if phrase in body_text:
            fail(f"recommendation page must not use marketplace language: {phrase}")

    # Header CTA on subpage should point back to home (no infinite self-link).
    header_cta = [a for a in parser.anchors if "header-cta" in (a.get("class") or "")]
    if not header_cta:
        fail("recommendation page must keep a header CTA (e.g. back to home)")
    if header_cta[0].get("href") == RECOMMENDATION_PATH:
        fail("recommendation page header CTA must not link to itself")


def assert_early_access_page(html: str) -> None:
    parser = parse(html)

    for landmark in ("header", "main", "footer", "nav"):
        if landmark not in parser.landmarks:
            fail(f"plan comparison page missing semantic landmark: {landmark}")

    # Must have a single data-access root.
    access_roots = [attrs for _, attrs in parser.elements if "data-access" in attrs]
    if len(access_roots) != 1:
        fail("plan comparison page needs exactly one data-access root")

    # Must render exactly three plan cards.
    cards = [
        attrs
        for _, attrs in parser.elements
        if "data-access-card" in attrs
    ]
    if len(cards) != 3:
        fail(
            "plan comparison page must render exactly three plan cards "
            f"(got {len(cards)})"
        )

    plan_keys = {attrs.get("data-plan") for attrs in cards if attrs.get("data-plan")}
    if plan_keys != {"current", "plus", "premium"}:
        fail(
            "plan cards must declare keys current/plus/premium; "
            f"got {sorted(plan_keys)}"
        )

    if any("data-emphasized" in attrs for attrs in cards):
        fail("plan featured treatment must be driven by selected state, not a fixed emphasized card")

    price_nodes = [
        attrs for _, attrs in parser.elements if "data-access-price" in attrs
    ]
    if len(price_nodes) != 3:
        fail("plan cards must expose three large price rows")

    if not all(text in html for text in ("Mevcut", "Plus", "Premium", "0 TL", "799 TL", "15 Gün", "1199 TL")):
        fail("plan comparison page must render Mevcut/Plus/Premium names and configured prices")

    selected_badges = [
        attrs for _, attrs in parser.elements if "data-access-selected-badge" in attrs
    ]
    if len(selected_badges) != 3:
        fail("plan cards must expose one selected-state badge hook per card")
    if sum(1 for attrs in selected_badges if "hidden" not in attrs) != 1:
        fail("plan comparison page must server-render exactly one visible selected badge")

    # Compact selected-note panel + context ribbon hooks.
    must_have_hooks = [
        "data-access-detail",
        "data-access-context",
        "data-access-context-default",
    ]
    for hook in must_have_hooks:
        if not any(hook in attrs for _, attrs in parser.elements):
            fail(f"plan comparison page must expose {hook}")

    context_nodes = [attrs for _, attrs in parser.elements if "data-access-context" in attrs]
    if "hidden" not in context_nodes[0]:
        fail("plan comparison context ribbon must be hidden by default before JS snapshot hydration")

    context_default_nodes = [
        attrs for _, attrs in parser.elements if "data-access-context-default" in attrs
    ]
    if "hidden" in context_default_nodes[0]:
        fail("plan comparison default context copy must be visible without JS")

    if re.search(r"data-access-[^>]+>\s*—\s*<", html):
        fail("plan comparison page must not server-render visible placeholder dash content")

    default_plan = access_roots[0].get("data-default-plan")
    if default_plan != "plus":
        fail("plan comparison must server-render Plus as the default selected plan")
    selected_cards = [
        attrs
        for attrs in cards
        if "is-selected" in (attrs.get("class") or "").split()
    ]
    if len(selected_cards) != 1 or selected_cards[0].get("data-plan") != default_plan:
        fail("plan comparison page must server-render exactly one selected default plan card")

    if any(attrs.get("tabindex") is not None for attrs in cards):
        fail("plan card articles must not create redundant tab stops")

    card_ctas = [attrs for attrs in parser.buttons if "data-access-card-cta" in attrs]
    if len(card_ctas) != 3:
        fail("plan comparison page must expose exactly three plan CTA buttons")
    if sum(1 for attrs in card_ctas if attrs.get("aria-pressed") == "true") != 1:
        fail("plan CTA buttons must expose exactly one selected aria-pressed state")
    for attrs in card_ctas:
        if attrs.get("aria-controls") != "access-detail":
            fail("plan CTA buttons must control the detail panel")
        if attrs.get("aria-pressed") not in {"true", "false"}:
            fail("plan CTA buttons must expose aria-pressed")
        if not attrs.get("data-label-default") or not attrs.get("data-label-selected"):
            fail("plan CTA buttons must keep stable default/selected labels")

    # No real form, no submit-capable buttons (cards are buttons but type=button).
    forms = [tag for tag, _ in parser.elements if tag == "form"]
    if forms:
        fail("plan comparison page must not contain a form element")

    for attrs in parser.buttons:
        button_type = (attrs.get("type") or "submit").casefold()
        if button_type == "submit":
            fail("plan comparison page must not expose submit-capable buttons")

    # No form controls.
    for tag, _attrs in parser.controls:
        if tag in {"input", "select", "textarea"}:
            fail(f"plan comparison page must not expose <{tag}> controls")

    # Header CTA must point home (not self).
    header_cta = [a for a in parser.anchors if "header-cta" in (a.get("class") or "")]
    if not header_cta:
        fail("plan comparison page must keep a header CTA")
    if header_cta[0].get("href") == EARLY_ACCESS_PATH:
        fail("plan comparison page header CTA must not link to itself")

    # Truth-safe / marketplace local guard for this surface.
    body_text = re.sub(r"<[^>]+>", " ", html).casefold()
    forbidden_local = [
        "satın al",
        "satın alın",
        "sepet",
        "kargo",
        "teslimat tarihi",
        "otomatik teslimat",
        "stok",
        "aboneliğin",
        "aboneliğiniz",
        "sepete ekle",
        "siparişi tamamla",
        "ücretsiz kargo",
        "stoklarla sınırlı",
        "ödeme adımına geç",
        "ödeme yapın",
        "aboneliğin başladı",
        "aboneliğiniz başladı",
        "üyeliğin aktif",
        "üyeliğiniz aktif",
        "premium'u yükselt",
        "premium'u seçin",
        "planınızı seçin",
        "mevcut planınız",
        "ilk kutunuz hazırlanıyor",
        "kampanya",
        "checkout'a git",
        "checkout başlat",
        "ai analiz",
        "ai takip",
        "uzman yönlendirmesi",
        "uzman onayı",
        "pediatrist onayladı",
        "topluluk rozeti",
        "dinamik fiyatlandırma",
        "mama ekleme",
        "oyuncak ekleme",
    ]
    for phrase in forbidden_local:
        if phrase in body_text:
            fail(
                "plan comparison page must not use unsupported marketplace/AI/expert language: "
                f"{phrase}"
            )


def assert_nav_progressive_enhancement(css: str) -> None:
    rules = css_rules(css)

    plain_site_nav_rules = rules_for_selector(rules, ".site-nav")
    if not plain_site_nav_rules:
        fail("site-nav needs a base no-JS rule")

    if any(declarations.get("display") == "none" for declarations in plain_site_nav_rules):
        fail("site-nav must not be hidden without the .js progressive-enhancement class")

    if not any(
        declarations.get("display") in {"flex", "grid", "block", "inline-flex"}
        for declarations in plain_site_nav_rules
    ):
        fail("site-nav needs a visible default display for no-JS users")

    plain_toggle_rules = rules_for_selector(rules, ".nav-toggle")
    if not any(declarations.get("display") == "none" for declarations in plain_toggle_rules):
        fail("nav-toggle needs a hidden no-JS default")

    visible_plain_toggle = [
        declarations.get("display")
        for declarations in plain_toggle_rules
        if declarations.get("display") in {"block", "flex", "grid", "inline-flex"}
    ]
    if visible_plain_toggle:
        fail("nav-toggle must only become visible under .js")

    js_site_nav_rules = rules_for_selector(rules, ".js .site-nav")
    if not any(declarations.get("display") == "none" for declarations in js_site_nav_rules):
        fail("JS-enhanced mobile nav needs a collapsed .js .site-nav rule")

    js_open_nav_rules = rules_for_selector(rules, ".js .site-nav.is-open")
    if not any(declarations.get("display") not in {None, "none"} for declarations in js_open_nav_rules):
        fail("JS-enhanced mobile nav needs a visible open state")

    js_toggle_rules = rules_for_selector(rules, ".js .nav-toggle")
    if not any(declarations.get("display") == "inline-flex" for declarations in js_toggle_rules):
        fail("nav-toggle must become visible only under .js")

    reveal_rules = rules_for_selector(rules, ".reveal")
    if not any(
        declarations.get("opacity") == "1" and declarations.get("transform") == "none"
        for declarations in reveal_rules
    ):
        fail("reveal items must be visible by default without JS")

    js_reveal_rules = rules_for_selector(rules, ".js .reveal")
    if not any(declarations.get("opacity") == "0" for declarations in js_reveal_rules):
        fail("reveal animation should only hide items after JS is active")


def assert_sticky_cta_mobile_only(css: str) -> None:
    rules = css_rules(css)

    base_rules = rules_for_selector(rules, ".sticky-cta")
    if not any(declarations.get("display") == "none" for declarations in base_rules):
        fail("sticky-cta must default to display:none outside mobile breakpoint")

    css_no_comments = re.sub(r"/\*.*?\*/", "", css, flags=re.DOTALL)
    mobile_block_match = re.search(
        r"@media\s*\(\s*max-width:\s*620px\s*\)\s*\{(.*)\}",
        css_no_comments,
        re.DOTALL,
    )
    if not mobile_block_match:
        fail("expected a @media (max-width: 620px) block for sticky-cta")

    mobile_block = mobile_block_match.group(1)
    sticky_in_mobile = re.search(
        r"\.sticky-cta\s*\{[^}]*display\s*:\s*block[^}]*\}",
        mobile_block,
    )
    if not sticky_in_mobile:
        fail("sticky-cta needs display:block inside the mobile breakpoint")


def assert_studio_snapshot_restart(js: str) -> None:
    if "sessionStorage.removeItem(SNAPSHOT_STORAGE_KEY)" not in js:
        fail("studio restart must clear the sessionStorage recommendation snapshot")
    if "restartBtn?.addEventListener" not in js or "clearSnapshot();" not in js:
        fail("studio restart handler must call clearSnapshot()")
    if "editBtn?.addEventListener" not in js:
        fail("studio edit handler must remain separate from restart")


def assert_early_access_dynamic_featured(js: str) -> None:
    required_snippets = {
        'card.classList.toggle("is-selected", isSelected)': "selected card class must be updated dynamically",
        "selectedBadge.hidden = !isSelected": "selected badge must move with selected card",
        "initialPlan = recommendedPlan": "snapshot plan must become the initial selected plan",
        "setRecommended(recommendedPlan)": "snapshot plan must receive the recommendation badge",
        'card.dataset.plan === planKey': "selection must use the requested plan key, not a fixed middle card",
    }
    for snippet, message in required_snippets.items():
        if snippet not in js:
            fail(f"plan dynamic featured guard failed: {message}")

    if 'querySelector("[data-access-card]:nth-child(2)")' in js:
        fail("plan selected/featured logic must not target the fixed middle card")


def markdown_files() -> list[Path]:
    candidates = [*ROOT.glob("*.md")]
    docs_dir = ROOT / "docs"
    if docs_dir.exists():
        candidates.extend(docs_dir.rglob("*.md"))
    return sorted(path for path in candidates if path.is_file())


def assert_doc_paths() -> None:
    real_pdf_dirname = "babie+ dosyaları"
    stale_pdf_dirname = "babie+ dosyalari"
    real_pdf_dir = ROOT / real_pdf_dirname
    if not real_pdf_dir.exists():
        fail(f"real PDF source directory is missing: {real_pdf_dirname}")

    pdf_references: set[str] = set()
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        if stale_pdf_dirname in text:
            fail(f"stale ASCII PDF path in {path.relative_to(ROOT)}")
        pdf_references.update(re.findall(r"babie\+ dosyaları/[^\s)>\"]+\.pdf", text))

    for reference in sorted(pdf_references):
        if not (ROOT / reference).exists():
            fail(f"markdown PDF reference does not exist: {reference}")


def main() -> None:
    for path in REQUIRED_FILES:
        if not path.exists():
            fail(f"missing {path.relative_to(ROOT)}")

    home_html = (DIST / "index.html").read_text(encoding="utf-8")
    studio_html = (DIST / "oneri" / "index.html").read_text(encoding="utf-8")
    access_html = (DIST / "erken-erisim" / "index.html").read_text(encoding="utf-8")
    css = (DIST / "assets" / "styles.css").read_text(encoding="utf-8")
    js = (DIST / "assets" / "app.js").read_text(encoding="utf-8")

    # Truth-safe copy must apply to all pages.
    for label, html in (
        ("home", home_html),
        ("recommendation", studio_html),
        ("early-access", access_html),
    ):
        normalized = re.sub(r"\s+", " ", html.casefold())
        for phrase in FORBIDDEN_COPY:
            if phrase.casefold() in normalized:
                fail(f"unsupported public claim found on {label} page: {phrase}")

    assert_home_page(home_html)
    assert_recommendation_page(studio_html)
    assert_early_access_page(access_html)
    assert_nav_progressive_enhancement(css)
    assert_sticky_cta_mobile_only(css)
    assert_studio_snapshot_restart(js)
    assert_early_access_dynamic_featured(js)
    assert_doc_paths()

    print(
        "Checks passed: home + recommendation + plan-comparison pages, landmarks, nav aria, "
        "contact links, studio guards, plan-comparison guards, no-JS nav guard, "
        "sticky-cta mobile guard, snapshot restart guard, plan dynamic featured guard, PDF paths, "
        "and truth-safe copy guard."
    )


if __name__ == "__main__":
    main()
