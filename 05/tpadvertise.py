#!/usr/bin/env python3
import sys
import tuxedo as t
import argparse

class Server:
    def tpsvrinit(self, argv):
        t.userlog(f"Starting server {argv}")
        parser = argparse.ArgumentParser()
        parser.add_argument('-i', dest='srvid')
        args, _ = parser.parse_known_args(argv)
        self.srvid = args.srvid
        t.tpadvertise(f'PING_{self.srvid}')
        return 0

    def PING_1(self, req):
        if self.srvid == '1':
            req['TA_DEBUG'] = "PING_1 called"
        else:
            req['TA_DEBUG'] = "PING_1 called but was not advertised"
        return t.tpreturn(t.TPSUCCESS, 0, req)

    def PING_2(self, req):
        if self.srvid == '2':
            req['TA_DEBUG'] = "PING_2 called"
        else:
            req['TA_DEBUG'] = "PING_2 called but was not advertised"
        return t.tpreturn(t.TPSUCCESS, 0, req)

    def UNADVERTISED(self, req):
        req['TA_DEBUG'] = "UNADVERTISED called"
        return t.tpreturn(t.TPSUCCESS, 0, req)

t.run(Server(), sys.argv)
