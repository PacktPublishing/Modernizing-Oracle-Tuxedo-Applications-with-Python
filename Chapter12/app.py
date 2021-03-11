#!/usr/bin/env python3

import sys
import tuxedo as t


class Server:
    def tpsvrinit(self, args):
        t.tpadvertise("TUX1")
        t.tpadvertise("TUX2")
        return 0

    def TUX1(self, data):
        if "TA_STATUS" not in data:
            data["TA_STATUS"] = []
        data["TA_STATUS"].append("Hello from TUX1")
        return t.tpreturn(t.TPSUCCESS, 0, data)

    def TUX2(self, data):
        if "TA_STATUS" not in data:
            data["TA_STATUS"] = []
        data["TA_STATUS"].append("Hello from TUX2")
        _, _, data = t.tpcall("NATS1", data, t.TPNOTRAN)
        return t.tpreturn(t.TPSUCCESS, 0, data)


if __name__ == "__main__":
    t.run(Server(), sys.argv)
