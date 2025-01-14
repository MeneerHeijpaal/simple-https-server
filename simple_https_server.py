#!/usr/bin/env python3
"""
Simple HTTPS server in python for logging GET and POST requests.                                           
Use this in combination with DNS Poisoning and a custom Root CA installed.

If this server is NOT trusted, most browsers and apps will not even connect.

Usage:
    ./server.py [<port>] - Defaults to port 443
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import ssl

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        print("#########################\n\n")

    def do_POST(self):
        content_length = int(self.headers.get('content-length', 0))
        post_data = self.rfile.read(content_length)

        self._set_response()
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))
        print("#########################\n\n")

def run(server_class=HTTPServer, handler_class=S, port=443):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    
    # Create SSL context
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile="server.pem", keyfile="key.pem")
    
    httpd = server_class(server_address, handler_class)
    
    try:
        # Wrap socket with SSL context
        httpd.socket = ssl_context.wrap_socket(httpd.socket,
                                               server_side=True)
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        logging.info('Stopping server...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
