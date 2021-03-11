#!/usr/bin/env python3
import sys
import tuxedo as t
import argparse


class Server:
    def tpsvrinit(self, argv):
        t.userlog(f"Starting server {argv}")
        setattr(self, "PING_1", self.UNADVERTISED)
        setattr(self, "PING_2", self.UNADVERTISED)
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", dest="srvid")
        args, _ = parser.parse_known_args(argv)
        self.srvid = args.srvid

        setattr(self, f"PING_{self.srvid}", self.PING)
        t.tpadvertise(f"PING_{self.srvid}")
        return 0

    def PING(self, req):
        req["TA_DEBUG"] = "PONG!"
        return t.tpreturn(t.TPSUCCESS, 0, req)

    def UNADVERTISED(self, req):
        req["TA_DEBUG"] = "UNADVERTISED called"
        return t.tpreturn(t.TPSUCCESS, 0, req)


t.run(Server(), sys.argv)
