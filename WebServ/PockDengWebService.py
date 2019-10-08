import http.server
import socketserver

import os

import sys
import webbrowser

PORT = 3510
Handler = http.server.SimpleHTTPRequestHandler

web_dir = os.path.join(os.path.dirname(__file__), './')
os.chdir(web_dir)

buffer = 1
sys.stderr = open('logfile.txt', 'w', buffer)

def Webserver():
    webbrowser.open('http://localhost:3510')
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        #print("serving at port", PORT)
        httpd.serve_forever()