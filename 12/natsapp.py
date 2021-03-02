import asyncio
import json
from nats.aio.client import Client

nc = Client()


async def NATS1(msg):
    req = json.loads(msg.data.decode())
    data = req["data"]
    if "TA_STATUS" not in data:
        data["TA_STATUS"] = []
    data["TA_STATUS"].append("Hello from NATS1")
    await nc.publish(
        msg.reply,
        json.dumps(
            {"rval": "TPSUCCESS", "rcode": 0, "data": data}
        ).encode(),
    )


async def NATS2(msg):
    req = json.loads(msg.data.decode())
    data = req["data"]
    if "TA_STATUS" not in data:
        data["TA_STATUS"] = []
    data["TA_STATUS"].append("Hello from NATS1")

    msg2 = await nc.request(
        "TUX1",
        json.dumps({"flags": "", "data": data}).encode(),
        timeout=5,
    )
    res = json.loads(msg2.data.decode())
    data = res["data"]

    await nc.publish(
        msg.reply,
        json.dumps(
            {"rval": "TPSUCCESS", "rcode": 0, "data": data}
        ).encode(),
    )


async def init(loop):
    await nc.connect(
        servers=["nats://host.docker.internal:4222"], loop=loop
    )
    await nc.subscribe("NATS1", cb=NATS1)
    await nc.subscribe("NATS2", cb=NATS2)


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
