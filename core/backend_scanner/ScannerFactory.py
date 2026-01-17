from core.backend_scanner.ExpressScanner import ExpressScanner
from core.backend_scanner.FastAPIScanner import FastAPIScanner
from core.backend_scanner.FlaskScanner import FlaskScanner

class ScannerFactory:

    def __init__(self):
        self.strategies = [
            ExpressScanner(),
            FastAPIScanner(),
            FlaskScanner(),
        ]

    def get_strategy(self, framework: str | None, files):
        if framework is not None:
            framework = framework.lower()

            for strategy in self.strategies:
                if strategy.name == framework:
                    return strategy

            raise ValueError(f"Unimplimented/Unknow framework: {framework}")

        for strategy in self.strategies:
            if strategy.detect(files):
                return strategy

        raise RuntimeError(
            "Could not detect backend framework. "
            "Please specify --framework explicitly."
        )

        
        
