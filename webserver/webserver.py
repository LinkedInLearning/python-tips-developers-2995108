import http.server
import socketserver

PORT = 8081

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("",PORT),handler) as ws:
    print("Webserver gestartet auf ", PORT)
    ws.serve_forever()