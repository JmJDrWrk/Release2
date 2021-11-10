import http.server
import socketserver
from threading import Thread
import os
# PORT = 8000
# DIRECTORY = "web"


class Server():
    def __init__(self, DIRECTORY, PORT):
        self.directory = DIRECTORY.replace(os.path.basename(DIRECTORY),'')
        self.port = PORT
        print('Joined Server Constructor')

    def start_server(self):
        def objetive():
            DIRECTORY = self.directory
            PORT = self.port

            class Handler(http.server.SimpleHTTPRequestHandler):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, directory=DIRECTORY, **kwargs)

            with socketserver.TCPServer(("", PORT), Handler) as httpd:
                print("serving at port", PORT)
                httpd.serve_forever()
        Thread(target=objetive).start()