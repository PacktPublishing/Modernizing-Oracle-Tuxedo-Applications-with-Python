#!/usr/bin/env python3
import sys
import tuxedo as t


class Server:
    def tpsvrinit(self, argv):
        t.userlog(f"Starting server {argv}")
        return 0

    def tpsvrthrinit(self, argv):
        t.userlog(f"Starting server thread {argv}")
        return 0

    def tpsvrdone(self):
        t.userlog(f"Stopping server")

    def tpsvrthrdone(self):
        t.userlog(f"Stopping server thread")

    def TOUPPER(self, req):
        return t.tpreturn(t.TPSUCCESS, 0, req.upper())


t.run(Server(), sys.argv)
