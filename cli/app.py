from cli.interactive import userQuaries, detectFramework
import sys
from pathlib import Path
from utils.files_utils import get_code_files
from core.backend_scanner.ScannerFactory import ScannerFactory
from core.backend_scanner.RouteScannerStrategy import Route, RouteScannerStrategy

def app():
    print("Welcome to Route Scanner.")
    print("Please answer the questions below to continue")
    
    detect = detectFramework()
    backend = None
    
    if detect:    
        try:
            result = userQuaries()
        except:
            print("The quaring has failed please try again.")
            sys.exit(1)
            
        backend = result['backend']
        frontend = result['frontend']
    
    root = Path(".")
    files = get_code_files(root)
    
    backendFramework: RouteScannerStrategy = ScannerFactory().get_strategy(backend, files)
    paths: list[Route] = backendFramework.scan()
    
    for path in paths:
        print(f"Method: {path.method}, Path: {path.path}, File: {path.file}")