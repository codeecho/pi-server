from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

import urlparse

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        f = open("index.html")
        self.wfile.write(f.read())

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        body = self.rfile.read(length)
        event = dict(urlparse.parse_qsl(body))
        self.wfile.write(handleEvent(event));

def handleEvent(event):
    return null;
        
def run(port=80):
    server_address = ('', port)
    httpd = HTTPServer(server_address, S)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    run()