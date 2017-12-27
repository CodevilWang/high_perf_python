import BaseHTTPServer
import urlparse
import time
from SocketServer import ThreadingMixIn
import threading
import sys


class WebRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")
        qdict = urlparse.parse_qs(urlparse.urlsplit(self.path).query)
        try:
            time.sleep(float(qdict["delay"][0]) / 1000.0)
        except Exception as e:
            sys.stderr.write("{} except {}".format(self.path, repr(e)))
            return

class ThreadingHttpServer(ThreadingMixIn, BaseHTTPServer.HTTPServer):
    pass


if __name__ == '__main__':
    # server = BaseHTTPServer.HTTPServer(('0.0.0.0',18460), WebRequestHandler)
    server = ThreadingHttpServer(('0.0.0.0', 8080), WebRequestHandler)
    ip, port = server.server_address
    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.setDaemon(True)
    server_thread.start()
    print "Server loop running in thread:", server_thread.getName()
    while True:
        pass
