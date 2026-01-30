import re

from pathlib import Path
from core.frontend_scanner.FrontendRouteScannerStrategy import FrontendRouteScannerStrategy, FrontRoute
from utils.files_utils import get_code_files

class NextjsScanner(FrontendRouteScannerStrategy):
    name = "react"

    def scan(self, root=None):
        return "react"
    
    
    def __find_server(self, root):
        files = get_code_files(root)
        
        server_match = None
        server_file = None
        for f in files:            
            text = f.read_text()
            
            regix = 'const (\w*) = express()'
            if server_match := re.search(regix, text):
                server_name = server_match.group(1)
                server_file = f
                break
            else:
                server_name = None
                server_file = None
            
        return server_name, server_file, text
    
    def __find_paths(self, server_name, server_file, text) -> list[FrontRoute]:
        current_file = Path(server_file)
        
        if server_name is not None:
            regix = fr'{server_name}.use\("(/\w*)", (\w*)\);'
            if routes_matchs := re.findall(regix, text):
                paths = self.__find_path_in_router(routes_matchs, current_file, text)
                
            paths = self.__find_path_in_server(paths, server_name, text, current_file)

        return paths
    
    def __find_path_in_router(self, routes_matchs, current_file, file_text) -> list[FrontRoute]:
        paths: list[FrontRoute] = []
                
        for routes in routes_matchs:
            route_path = routes[0]
            route_name = routes[1]
            
            regix = fr'import {route_name} from "\./(.*)"'
            if route_files := re.search(regix, file_text):
                route_files = current_file.parent / route_files[1]
                try:
                    with open(route_files) as route_file:
                        text = route_file.read()
                        
                    route_regix = fr'.*\.(get|post|put|delete|patch)\(\"(.*)\", \w*\);'
                    
                    if matchs := re.findall(route_regix, text):
                        for m in matchs:
                            method = m[0]
                            path = route_path + m[1]
                            
                            route = FrontRoute(method=method, path=path, file=route_file.name)
                            paths.append(route)
                        
                except FileNotFoundError:
                    pass
                        
        return paths
    
    
    def __find_path_in_server(self, paths, server_name, server_text, server_path) -> list[FrontRoute]: 
        route_in_server_regix = fr'{server_name}\.(get|post|put|delete|patch)\(\"(.*)\", .*'
        
        if match := re.findall(route_in_server_regix, server_text):
            for m in match:
                method = m[0]
                path = m[1]

                route = FrontRoute(method=method, path=path, file=str(server_path))
                paths.append(route)
                
                
        return paths