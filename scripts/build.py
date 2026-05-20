import os
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


ROUTE_TOKEN_PREFIX = "@route:"


def normalize_base_path(raw_base_path: str | None) -> str:
    if raw_base_path is None:
        return "/"

    base_path = raw_base_path.strip()
    if not base_path or base_path == "/":
        return "/"
    if "://" in base_path:
        raise ValueError("BABIE_SITE_BASE_PATH must be a path, not a full URL")

    return "/" + base_path.strip("/") + "/"


def build_path_map(base_path: str) -> dict[str, str]:
    return {
        "home": base_path,
        "recommendation": f"{base_path}oneri/",
        "early_access": f"{base_path}erken-erisim/",
    }


def resolve_route_token(value: str, path_map: dict[str, str]) -> str:
    if not value.startswith(ROUTE_TOKEN_PREFIX):
        return value

    route_key, hash_marker, anchor = value.removeprefix(ROUTE_TOKEN_PREFIX).partition("#")
    if route_key not in path_map:
        raise KeyError(f"Unknown route token: {value}")

    resolved = path_map[route_key]
    if hash_marker:
        return f"{resolved}#{anchor}"
    return resolved


def resolve_routes(value, path_map: dict[str, str]):
    if isinstance(value, dict):
        return {key: resolve_routes(item, path_map) for key, item in value.items()}
    if isinstance(value, list):
        return [resolve_routes(item, path_map) for item in value]
    if isinstance(value, tuple):
        return tuple(resolve_routes(item, path_map) for item in value)
    if isinstance(value, str):
        return resolve_route_token(value, path_map)
    return value


def copy_static() -> None:
    assets_dir = DIST / "assets"
    if assets_dir.exists():
        shutil.rmtree(assets_dir)
    shutil.copytree(SRC / "static", assets_dir)


def expand_nav(nav: list[dict], home_path: str, use_local_anchors: bool) -> list[dict]:
    """Expand slug-based nav items to the correct home anchor targets."""
    expanded = []
    for item in nav:
        slug = item.get("slug")
        if slug is None:
            href = item.get("href", "#")
        elif use_local_anchors:
            href = f"#{slug}"
        else:
            href = f"{home_path}#{slug}"
        expanded.append({"label": item["label"], "href": href})
    return expanded


def render_page(env: Environment, template_name: str, context: dict, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    html = env.get_template(template_name).render(**context)
    output.write_text(html, encoding="utf-8")


def build() -> None:
    base_path = normalize_base_path(os.getenv("BABIE_SITE_BASE_PATH"))
    path_map = build_path_map(base_path)

    env = Environment(
        loader=FileSystemLoader(SRC / "templates"),
        autoescape=select_autoescape(("html", "xml")),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    DIST.mkdir(exist_ok=True)

    home_content = resolve_routes(HOME, path_map)
    recommendation_content = resolve_routes(RECOMMENDATION, path_map)
    early_access_content = resolve_routes(EARLY_ACCESS, path_map)

    # Home page: assets at ./assets/, nav anchors stay local (#slug).
    home_context = {
        **home_content,
        "nav": expand_nav(HOME["nav"], home_path=path_map["home"], use_local_anchors=True),
        "asset_prefix": "assets",
        "home_path": path_map["home"],
        "recommendation_path": path_map["recommendation"],
        "early_access_path": path_map["early_access"],
        "current_page": "home",
    }
    render_page(env, "index.html", home_context, DIST / "index.html")

    # Recommendation page lives in /oneri/index.html. Assets are referenced via
    # ../assets to keep them shared with the home page.
    recommendation_context = {
        **recommendation_content,
        "nav": expand_nav(
            RECOMMENDATION["nav"],
            home_path=path_map["home"],
            use_local_anchors=False,
        ),
        "asset_prefix": "../assets",
        "home_path": path_map["home"],
        "recommendation_path": path_map["recommendation"],
        "early_access_path": path_map["early_access"],
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
        **early_access_content,
        "nav": expand_nav(
            EARLY_ACCESS["nav"],
            home_path=path_map["home"],
            use_local_anchors=False,
        ),
        "asset_prefix": "../assets",
        "home_path": path_map["home"],
        "recommendation_path": path_map["recommendation"],
        "early_access_path": path_map["early_access"],
        "current_page": "early-access",
    }
    render_page(
        env,
        "early_access.html",
        early_access_context,
        DIST / "erken-erisim" / "index.html",
    )

    copy_static()

    (DIST / ".nojekyll").write_text("", encoding="utf-8")

    print(f"Built {DIST / 'index.html'}")
    print(f"Built {DIST / 'oneri' / 'index.html'}")
    print(f"Built {DIST / 'erken-erisim' / 'index.html'}")


if __name__ == "__main__":
    build()
