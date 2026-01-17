from pathlib import Path
from typing import List, Tuple

CODE_EXTENSIONS: Tuple[str, ...] = (".py", ".js", ".ts", ".jsx", ".tsx")

IGNORE_DIRS: Tuple[str, ...] = ("node_modules", "__pycache__", ".git", ".venv")

IGNORE_FILES_PREFIX: Tuple[str, ...] = (".",)

BINARY_EXTENSIONS: Tuple[str, ...] = (
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".exe", ".dll", ".so", ".dylib"
)

def get_code_files(root: Path) -> List[Path]:
    files = []
    for f in root.rglob("*"):
        if not f.is_file():
            continue
        if f.name.startswith(IGNORE_FILES_PREFIX):
            continue
        if any(part in IGNORE_DIRS for part in f.parts):
            continue
        if f.suffix.lower() in BINARY_EXTENSIONS:
            continue
        if f.suffix.lower() not in CODE_EXTENSIONS:
            continue
        
        files.append(f)
    return files
