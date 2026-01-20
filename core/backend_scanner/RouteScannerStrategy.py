from abc import ABC, abstractmethod
from pathlib import Path
from pydantic.dataclasses import dataclass

@dataclass
class Route:
    method: str
    path: str
    file: str

class RouteScannerStrategy(ABC):
    name: str

    def detect(self, files: list[Path]) -> bool:
        """Return True if this framework is likely used"""
        return any(self.name in f.read_text() for f in files)

    @abstractmethod
    def scan(self, root: Path) -> list[Route]:
        """Extract all routes from the codebase"""
        pass
