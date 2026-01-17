from cli.interactive import userQuaries

def app():
    result = userQuaries()
    backend = result['backend']
    frontend = result['frontend']
    
    