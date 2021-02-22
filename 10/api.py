#!/usr/bin/env python3
import sys
import http.server
import socketserver
import json
import threading

import tuxedo as t


class Handler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content = self.rfile.read(
            int(self.headers.get("Content-Length", "0"))
        )
        req = json.loads(content)
        _, _, res = t.tpcall(self.path[1:], req)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(res).encode("utf-8"))


def serve():
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(
        ("", 8000), Handler
    ) as httpd:
        httpd.serve_forever()


class Server:
    def tpsvrinit(self, args):
        threading.Thread(target=serve, daemon=True).start()
        return 0


if __name__ == "__main__":
    t.run(Server(), sys.argv)
