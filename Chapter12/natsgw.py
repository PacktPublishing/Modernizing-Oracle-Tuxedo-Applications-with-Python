#!/usr/bin/env python3

import asyncio
import json
import sys
import threading

import tuxedo as t
from nats.aio.client import Client

nc = Client()
loop = asyncio.get_event_loop()


async def on_message(msg):
    req = json.loads(msg.data.decode())
    svcname = msg.subject
    data = req["data"]

    try:
        rval, rcode, data = await loop.run_in_executor(
            None, t.tpcall, svcname, data
        )
    except t.XatmiException:
        rval, rcode, data = t.TPESVCFAIL, 0, None

    await nc.publish(
        msg.reply,
        json.dumps(
            {
                "rval": "TPFAIL"
                if rval == t.TPESVCFAIL
                else "TPSUCCESS",
                "rcode": rcode,
                "data": data,
            }
        ).encode(),
    )


async def on_service(name, data, flags):
    if flags & t.TPTRAN:
        return (t.TPFAIL, 0, data)

    try:
        msg = await nc.request(
            name,
            json.dumps({"flags": "", "data": data}).encode(),
            timeout=5,
        )
        res = json.loads(msg.data.decode())
        return (
            t.TPSUCCESS if res["rval"] == "TPSUCCESS" else t.TPFAIL,
            res["rcode"],
            res["data"],
        )
    except asyncio.TimeoutError:
        return (t.TPFAIL, 0, data)


class Server:
    def tpsvrinit(self, args):
        threading.Thread(
            target=loop.run_forever, daemon=True
        ).start()
        asyncio.run_coroutine_threadsafe(
            nc.connect(
                servers=["nats://host.docker.internal:4222"],
                loop=loop,
            ),
            loop,
        ).result()

        setattr(self, "NATS1", self.PROXY)
        t.tpadvertise("NATS1")
        setattr(self, "NATS2", self.PROXY)
        t.tpadvertise("NATS2")

        asyncio.run_coroutine_threadsafe(
            nc.subscribe("TUX1", cb=on_message), loop
        ).result()
        asyncio.run_coroutine_threadsafe(
            nc.subscribe("TUX2", cb=on_message), loop
        ).result()

        return 0

    def PROXY(self, data, name, flags):
        future = asyncio.run_coroutine_threadsafe(
            on_service(name, data, flags), loop
        )
        rval, rcode, data = future.result(timeout=5)
        return t.tpreturn(rval, rcode, data)


if __name__ == "__main__":
    t.run(Server(), sys.argv)
