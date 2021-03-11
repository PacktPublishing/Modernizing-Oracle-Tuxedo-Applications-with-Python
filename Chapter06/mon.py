import os
import tuxedo as t


def getall(req):
    res = t.tpcall(".TMIB", req).data
    out = res
    while res["TA_MORE"][0] > 0:
        req["TA_OPERATION"] = "GETNEXT"
        req["TA_CURSOR"] = res["TA_CURSOR"]
        res = t.tpcall(".TMIB", req).data
        for k, v in res.items():
            out[k].extend(v)

    return out


server = getall(
    {
        "TA_CLASS": "T_SERVER",
        "TA_OPERATION": "GET",
        "TA_FLAGS": t.MIB_LOCAL,
    }
)
client = getall(
    {
        "TA_CLASS": "T_CLIENT",
        "TA_OPERATION": "GET",
        "TA_FLAGS": t.MIB_LOCAL,
    }
)
msg = getall(
    {
        "TA_CLASS": "T_MSG",
        "TA_OPERATION": "GET",
        "TA_FLAGS": t.MIB_LOCAL,
    }
)

processes = {}
for i in range(len(server["TA_PID"])):
    processes[server["TA_PID"][i]] = os.path.basename(
        server["TA_SERVERNAME"][i]
    )
for pid in client["TA_PID"]:
    processes[pid] = "client#{}".format(pid)

for i in range(len(msg["TA_CURTIME"])):
    print(
        "{} : {} -> [{} msg {}/{} bytes] -> {}".format(
            max(msg["TA_MSG_RTIME"][i], msg["TA_MSG_STIME"][i]),
            processes.get(
                msg["TA_MSG_LRPID"][i], msg["TA_MSG_LRPID"][i]
            ),
            msg["TA_MSG_QNUM"][i],
            msg["TA_MSG_CBYTES"][i],
            msg["TA_MSG_QBYTES"][i],
            processes.get(
                msg["TA_MSG_LSPID"][i], msg["TA_MSG_LSPID"][i]
            ),
        )
    )
