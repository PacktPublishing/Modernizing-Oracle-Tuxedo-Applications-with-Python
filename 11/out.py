#!/usr/bin/env python3

import socket
import sys
import threading
import time
import tuxedo as t


class Server:
    def tpsvrinit(self, args):
        t.tpadvertise("TOUPPER")
        self.lock = threading.Lock()
        self.counter = 0
        self.sock = socket.create_connection(
            ("127.0.0.1", 8765)
        )
        threading.Thread(
            target=self.ping, daemon=True
        ).start()
        return 0

    def ping(self):
        while True:
            time.sleep(60)
            with self.lock:
                self.sock.sendall(b"ping")
                assert len(self.sock.recv(4)) == 4

    def TOUPPER(self, data):
        req = data.encode()
        with self.lock:
            self.sock.sendall(req)
            res = self.sock.recv(len(req))
            assert len(res) == len(req)
        return t.tpreturn(t.TPSUCCESS, 0, res.decode())


if __name__ == "__main__":
    t.run(Server(), sys.argv)
