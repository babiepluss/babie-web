from pathlib import Path
import shutil
import sys

from jinja2 import Environment, FileSystemLoader, select_autoescape

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
DIST = ROOT / "dist"

sys.path.insert(0, str(ROOT))
from src.content.home import HOME, RECOMMENDATION, EARLY_ACCESS  # noqa: E402


def copy_static() -> None:
    assets_dir = DIST / "assets"
    if assets_dir.exists():
        shutil.rmtree(assets_dir)
    shutil.copytree(SRC / "static", assets_dir)


def expand_nav(nav: list[dict], home_prefix: str) -> list[dict]:
    """Expand slug-based nav items to anchor href values for the current page.

    home_prefix should be "" when rendering home (anchors stay local with #),
    and "/" when rendering a subpage so that nav links point back to the home
    section anchors.
    """
    expanded = []
    for item in nav:
        slug = item.get("slug")
        if slug is None:
            href = item.get("href", "#")
        else:
            href = f"{home_prefix}#{slug}"
        expanded.append({"label": item["label"], "href": href})
    return expanded


def render_page(env: Environment, template_name: str, context: dict, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    html = env.get_template(template_name).render(**context)
    output.write_text(html, encoding="utf-8")


def build() -> None:
    env = Environment(
        loader=FileSystemLoader(SRC / "templates"),
        autoescape=select_autoescape(("html", "xml")),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    DIST.mkdir(exist_ok=True)

    # Home page: assets at ./assets/, nav anchors stay local (#slug),
    # and recommendation experience lives at /oneri/.
    home_context = {
        **HOME,
        "nav": expand_nav(HOME["nav"], home_prefix=""),
        "asset_prefix": "assets",
        "home_path": "/",
        "recommendation_path": "/oneri/",
        "current_page": "home",
    }
    render_page(env, "index.html", home_context, DIST / "index.html")

    # Recommendation page lives in /oneri/index.html so it serves at /oneri/
    # under the simple http.server. Assets are referenced via ../assets to
    # keep them shared with the home page.
    recommendation_context = {
        **RECOMMENDATION,
        "nav": expand_nav(RECOMMENDATION["nav"], home_prefix="/"),
        "asset_prefix": "../assets",
        "home_path": "/",
        "recommendation_path": "/oneri/",
        "current_page": "recommendation",
    }
    render_page(
        env,
        "recommendation.html",
        recommendation_context,
        DIST / "oneri" / "index.html",
    )

    # Early access tier comparison page lives at /erken-erisim/.
    early_access_context = {
        **EARLY_ACCESS,
        "nav": expand_nav(EARLY_ACCESS["nav"], home_prefix="/"),
        "asset_prefix": "../assets",
        "home_path": "/",
        "recommendation_path": "/oneri/",
        "early_access_path": "/erken-erisim/",
        "current_page": "early-access",
    }
    render_page(
        env,
        "early_access.html",
        early_access_context,
        DIST / "erken-erisim" / "index.html",
    )

    copy_static()

    print(f"Built {DIST / 'index.html'}")
    print(f"Built {DIST / 'oneri' / 'index.html'}")
    print(f"Built {DIST / 'erken-erisim' / 'index.html'}")


if __name__ == "__main__":
    build()
