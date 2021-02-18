#!/usr/bin/env python3
import sys
import tuxedo as t
import cx_Oracle
import uuid


class Server:
    def tpsvrinit(self, argv):
        t.tpadvertise("STORE")
        t.tpadvertise("COUNTXA")
        self.db = cx_Oracle.connect(handle=t.xaoSvcCtx())
        return 0

    def STORE(self, req):
        with self.db.cursor() as dbc:
            dbc.execute(
                "INSERT INTO messages VALUES (:1, :2)",
                [str(uuid.uuid4()), req["TA_SOURCE"][0]],
            )
        return t.tpreturn(t.TPSUCCESS, 0, req)

    def COUNTXA(self, req):
        with self.db.cursor() as dbc:
            dbc.execute("SELECT COUNT(1) FROM messages")
            req["TA_STATUS"] = "Count={}".format(dbc.fetchone()[0])
        return t.tpreturn(t.TPSUCCESS, 0, req)


t.run(Server(), sys.argv, "Oracle_XA")
