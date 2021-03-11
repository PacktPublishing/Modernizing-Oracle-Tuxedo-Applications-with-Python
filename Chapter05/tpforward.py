#!/usr/bin/env python3
import sys
import tuxedo as t


class Server:
    def tpsvrinit(self, argv):
        t.tpadvertise("WORK")
        t.tpadvertise("POSTPROC")
        return 0

    def WORK(self, data):
        data["TA_DEBUG"] = []
        data["TA_DEBUG"].append("WORK called")
        return t.tpforward("POSTPROC", data)

    def POSTPROC(self, data):
        data["TA_DEBUG"].append("POSTPROC called")
        return t.tpreturn(t.TPSUCCESS, 0, data)


t.run(Server(), sys.argv)
