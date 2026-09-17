"""Databricks SA Dev Kit."""
from pathlib import Path


def _version():
    try:
        from importlib.metadata import version

        return version("databricks-sa-kit")
    except Exception:
        pass
    # repo checkout: read VERSION at the toolkit root
    for cand in Path(__file__).resolve().parents:
        vf = cand / "VERSION"
        if vf.is_file():
            return vf.read_text(encoding="utf-8").strip()
    return "0.0.0"


__version__ = _version()
