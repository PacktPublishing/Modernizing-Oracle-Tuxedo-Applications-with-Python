#!/usr/bin/env python3
import sys
import tuxedo as t


class Server:
    def tpsvrinit(self, argv):
        t.tpadvertise("REQ")
        return 0

    def REQ(self, req):
        req["TA_STATUS"] = "done"
        return t.tpreturn(t.TPSUCCESS, 0, req)


t.run(Server(), sys.argv)
