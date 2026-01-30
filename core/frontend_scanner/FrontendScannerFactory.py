from core.frontend_scanner.ReactScanner import ReactScanner
from core.frontend_scanner.NextjsScanner import NextjsScanner

class FrontendScannerFactory:

    def __init__(self):
        self.strategies = [
            ReactScanner(),
            NextjsScanner()
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

        
        
