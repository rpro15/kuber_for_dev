from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
from os import name
import sys

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        now = datetime.now()
        response_string = now.strftime("The time is %-I:%M %p, UTC.")
        self.wfile.write(bytes(response_string, "utf-8"))

def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port 8000...')
    httpd.serve_forever()

if __name__ == "__main__":
      run()