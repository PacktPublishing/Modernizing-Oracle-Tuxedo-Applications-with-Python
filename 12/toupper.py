import asyncio
from nats.aio.client import Client

nc = Client()


async def TOUPPER(msg):
    await nc.publish(msg.reply, msg.data.decode().upper().encode())


async def run(loop):
    await nc.connect(
        servers=["nats://host.docker.internal:4222"], loop=loop
    )
    await nc.subscribe("TOUPPER", cb=TOUPPER)

    try:
        msg = await nc.request(
            "TOUPPER",
            "Hello NATS.io!".encode(),
            timeout=5,
        )
        print(msg.data.decode())
    except asyncio.TimeoutError:
        print("Timed out waiting for response")

    await nc.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(run(loop))
loop.close()
