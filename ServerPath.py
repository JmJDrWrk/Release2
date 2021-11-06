from termcolor import colored
import os
from threading import Thread
# from http.server import HTTPServer as BaseHTTPServer, SimpleHTTPRequestHandler
# import win32comext.shell.shell as shell
import subprocess
class ServerPath():
    def __init__(self):
        print(colored('ServerPath constructor joined', 'blue'))

    def ServePathAtNewThread(PATH, PORT):
        state = 'OFF'
        def objetive():
            #print(colored(f'SERVER at port: {PORT}', 'cyan'))
            basepath = PATH.replace(("\\"+os.path.basename(PATH)), "")
            server_setup = f'cd \\ && cd {basepath} && python -m http.server {PORT}'
            #print(colored(server_setup, 'red'))
            #os.chdir(basepath)
            # subprocess.Popen(server_setup,shell=True,stdout=subprocess.STDOUT,stderr=subprocess.STDOUT,stdin=subprocess.DEVNULL)
            subprocess.call(f'python -m http.server {PORT}', shell=True, cwd=basepath)
            #os.system(f'python -m http.server {PORT}')

        try:
            Thread(target=objetive).start()
            state = 'ON'
        except:
            print(colored('Server setup error', 'red'))
            state = 'OFF'

        return state
    
    # def ServerPathAdvancedMode(PATH, PORT):
    #     class HTTPHandler(SimpleHTTPRequestHandler):
    #         """This handler uses server.base_path instead of always using os.getcwd()"""
    #         def translate_path(self, path):
    #             path = SimpleHTTPRequestHandler.translate_path(self, path)
    #             relpath = os.path.relpath(path, os.getcwd())
    #             fullpath = os.path.join(self.server.base_path, relpath)
    #             return fullpath
        
    #     class HTTPServer(BaseHTTPServer):
    #         """The main server, you pass in base_path which is the path you want to serve requests from"""
    #         def __init__(self, base_path, server_address, RequestHandlerClass=HTTPHandler):
    #             self.base_path = base_path
    #             BaseHTTPServer.__init__(self, server_address, RequestHandlerClass)

    #     web_dir = PATH.replace('\\'+os.path.basename(PATH),'')
    #     httpd = HTTPServer(web_dir, ("", PORT))
    #     #httpd.serve_forever()

    # def ServePathAtNewThreadUsingShell(PATH, PORT):
    #     state = 'OFF'
    #     def objetive():
    #         #print(colored(f'SERVER at port: {PORT}', 'cyan'))
    #         basepath = PATH.replace(("\\"+os.path.basename(PATH)), "")
    #         server_setup = f'cd \\ && cd {basepath} && python -m http.server {PORT}'
    #         print(colored(server_setup, 'red'))
            
    #     try:
    #         Thread(target=objetive).start()
    #         state = 'ON'
    #     except:
    #         print(colored('Server setup error', 'red'))
    #         state = 'OFF'

    #     return state