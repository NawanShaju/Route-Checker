from cli.interactive import userQuaries
import sys
from pathlib import Path

from core.backend_scanner.ScannerFactory import ScannerFactory

def app():
    
    print("Welcome to Route Scanner.")
    print("Please answer the questions below to continue")
    
    try:
        result = userQuaries()
    except:
        print("The quaring has failed please try again.")
        sys.exit(1)
        
    
    backend = result['backend']
    frontend = result['frontend']
    
    files = [Path(".")]
    backendFramework = ScannerFactory().get_strategy(backend, files)
    print(backendFramework.name)
    