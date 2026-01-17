from cli.interactive import userQuaries
import sys

def app():
    
    print("Welcome to Route Scanner.")
    print("Please answer the questions below to continue")
    
    try:
        result = userQuaries()
    except:
        print("The quaring has failed please run the code again.")
        sys.exit(1)
        
    
    backend = result['backend']
    frontend = result['frontend']
    
    
    print(backend)
    print(frontend)
    