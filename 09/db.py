#!/usr/bin/env python3
import sys
import tuxedo as t
import cx_Oracle


class Server:
    def tpsvrinit(self, argv):
        t.tpadvertise("COUNT")
        self.db = cx_Oracle.connect(
            "tuxedo",
            "tuxpass",
            "host.docker.internal:32769/ORCLPDB1.localdomain",
        )
        return 0

    def COUNT(self, req):
        with self.db.cursor() as dbc:
            dbc.execute("SELECT COUNT(1) FROM messages")
            req["TA_STATUS"] = "Count={}".format(dbc.fetchone()[0])
        return t.tpreturn(t.TPSUCCESS, 0, req)


t.run(Server(), sys.argv)
