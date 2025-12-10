from pathlib import Path

__all__ = ["get_project_root", "get_assets_dir", "get_asset_path"]


def get_project_root() -> Path:
    return Path(__file__).resolve().parents[3]


def get_assets_dir() -> Path:
    return get_project_root() / "tests" / "ui" / "assets"


def get_asset_path(filename: str) -> Path:
    return get_assets_dir() / filename

