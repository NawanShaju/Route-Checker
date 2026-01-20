from core.backend_scanner.RouteScannerStrategy import RouteScannerStrategy

class FastAPIScanner(RouteScannerStrategy):
    name = "fastapi"

    def scan(self, root=None):
        return "routes"
