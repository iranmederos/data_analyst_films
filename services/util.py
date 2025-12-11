# services/util.py

import json
from pathlib import Path
from typing import Any

ARTIFACTS_DIR = Path("artifacts")


def _resolve_path(dir_file: str | Path) -> Path:
    path = Path(dir_file)
    return path if path.is_absolute() else ARTIFACTS_DIR / path


def generate_response(dir_file: str | Path) -> Any:
    path = _resolve_path(dir_file)
    if not path.exists():
        msg = f"Archivo no encontrado en la ruta {path} porfavor crearlo en el notebook."
        return {"error": msg}
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except json.JSONDecodeError:
        msg = f"Fallo al parsear la informacion en la ruta {path}."
        return {"error": msg}
