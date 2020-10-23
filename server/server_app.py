#!/usr/bin/python

from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(str("<html><head><title>https://pythonbasics.org</title></head>").encode("utf-8"))
        self.wfile.write(str("<p>Request: {}</p>".format(self.path)).encode("utf-8"))
        self.wfile.write(str("<body>").encode("utf-8"))
        self.wfile.write(str("<p>This is an example web server.</p>").encode("utf-8"))
        self.wfile.write(str("</body></html>").encode("utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")