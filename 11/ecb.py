#!/usr/bin/env python3

import sys
import urllib.request
from xml.etree import ElementTree as et

import tuxedo as t


class Server:
    def tpsvrinit(self, args):
        t.tpadvertise("GETRATES")
        t.tpadvertise("GETRATES_LATER")
        t.tpadvertise("GETRATES_DONE")
        return 0

    def GETRATES(self, data):
        try:
            f = urllib.request.urlopen(
                "https://www.ecb.europa.eu"
                + "/stats/eurofxref/eurofxref-daily.xml",
                timeout=10,
            )
            rates = et.fromstring(f.read().decode("utf8"))
            data["TA_STATE"] = ""
            for r in rates.findall(".//*[@currency]"):
                data["TA_STATE"] += "{}={};".format(
                    r.attrib["currency"], r.attrib["rate"]
                )
        except:
            return t.tpreturn(t.TPFAIL, 0, {})
        else:
            return t.tpreturn(t.TPSUCCESS, 0, data)


if __name__ == "__main__":
    t.run(Server(), sys.argv)
