import time
import tuxedo as t

seconds = int(time.time())
status = []
while True:
    status.extend(t.tpcall("PING", {}).data["TA_STATUS"])
    if seconds != int(time.time()):
        print(
            "{} | cps={} | status={}".format(
                time.ctime(seconds), len(status), set(status)
            )
        )
        seconds = int(time.time())
        status = []
    time.sleep(0.01)
