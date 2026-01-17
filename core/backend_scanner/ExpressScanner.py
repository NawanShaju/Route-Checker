from core.backend_scanner.RouteScannerStrategy import RouteScannerStrategy

class ExpressScanner(RouteScannerStrategy):
    name = "express"

    def scan(self, root):
        return "routes"
