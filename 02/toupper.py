#!/usr/bin/env python3
import sys
import tuxedo as t

class Server:
    def TOUPPER(self, req):
        return t.tpreturn(t.TPSUCCESS, 0, req.upper())

t.run(Server(), sys.argv)
