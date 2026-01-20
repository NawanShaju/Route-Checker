from core.backend_scanner.RouteScannerStrategy import RouteScannerStrategy

class FlaskScanner(RouteScannerStrategy):
    name = "flask"

    def scan(self, root=None):
        return "routes"
