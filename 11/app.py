#!/usr/bin/env python3

import sys
import tuxedo as t


class Server:
    def tpsvrinit(self, args):
        t.tpadvertise("GETRATES_ASYNC")
        t.tpadvertise("GETRATES_DONE")
        return 0

    def GETRATES_ASYNC(self, data):
        t.tpenqueue(
            "QSPACE",
            "GETRATES",
            t.TPQCTL(replyqueue="GETRATES_DONE", flags=t.TPQREPLYQ),
            data,
        )
        return t.tpreturn(t.TPSUCCESS, 0, {})

    def GETRATES_DONE(self, data):
        t.userlog(data["TA_STATE"][0])
        return t.tpreturn(t.TPSUCCESS, 0, {})


if __name__ == "__main__":
    t.run(Server(), sys.argv)
