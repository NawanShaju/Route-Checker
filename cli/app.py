from cli.interactive import userQuaries, detectFramework
import sys
from pathlib import Path
import os

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
    files = [f for f in root.rglob("*") if f.is_file()]

    backendFramework = ScannerFactory().get_strategy(backend, files)
    print(backendFramework.name)
    