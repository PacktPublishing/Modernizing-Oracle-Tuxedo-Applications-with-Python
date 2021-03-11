#!/usr/bin/env python3
import sys
import tuxedo as t


class Server:
    def tpsvrinit(self, argv):
        t.tpadvertise("PING")
        return 0

    def PING(self, req):
        req["TA_STATUS"] = "v1"
        return t.tpreturn(t.TPSUCCESS, 0, req)


t.run(Server(), sys.argv)
