#!/usr/bin/env python3
import sys
import time
import tuxedo as t


class Server:
    def tpsvrinit(self, argv):
        t.tpadvertise("PING")
        t.tpadvertise("SLEEP")
        return 0

    def PING(self, req, flags):
        if flags & t.TPTRAN:
            t.userlog("PING in a transaction")
        else:
            t.userlog("PING outside a transaction")
        req["TA_STATUS"] = "v1"
        return t.tpreturn(t.TPSUCCESS, 0, req)

    def SLEEP(self, req, flags):
        for _ in range(10):
            t.userlog("tpgetlev()={}".format(t.tpgetlev()))
            time.sleep(1)
        t.userlog("tpgetlev()={} before".format(t.tpgetlev()))
        try:
            t.tpcall("PING", {})
        except t.XatmiException as e:
            t.userlog("Got error {}".format(e))
        t.userlog("tpgetlev()={} after".format(t.tpgetlev()))
        return t.tpreturn(t.TPSUCCESS, 0, req)


t.run(Server(), sys.argv)
