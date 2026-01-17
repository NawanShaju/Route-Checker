from cli.interactive import userQuaries, detectFramework
import sys
from pathlib import Path
from utils.files_utils import get_code_files
from core.backend_scanner.ScannerFactory import ScannerFactory

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
    
    backendFramework = ScannerFactory().get_strategy(backend, files)
    print(backendFramework.name, backend)
    