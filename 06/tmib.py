import tuxedo as t


def check(res):
    if res["TA_ERROR"][0] < 0:
        for i in res.get("TA_BADFLD", []):
            print("Bad field:", t.Fname32(i))
        print("Status:", res["TA_STATUS"][0])
        assert False


t.tpcall(
    ".TMIB",
    {
        "TA_CLASS": "T_GROUP",
        "TA_OPERATION": "SET",
        "TA_STATE": "NEW",
        "TA_SRVGRP": "GROUP2",
        "TA_GRPNO": 2,
        "TA_LMID": "tuxapp",
    },
)
t.tpcall(
    ".TMIB",
    {
        "TA_CLASS": "T_GROUP",
        "TA_OPERATION": "SET",
        "TA_STATE": "ACT",
        "TA_SRVGRP": "GROUP2",
    },
)

t.tpcall(
    ".TMIB",
    {
        "TA_CLASS": "T_SERVER",
        "TA_OPERATION": "SET",
        "TA_STATE": "NEW",
        "TA_SRVGRP": "GROUP2",
        "TA_SERVERNAME": "ping2.py",
        "TA_SRVID": 10,
        "TA_MIN": 5,
        "TA_MAX": 5,
        "TA_REPLYQ": "Y",
        "TA_MAXGEN": 2,
        "TA_RESTART": "Y",
        "TA_GRACE": 0,
        "TA_RQADDR": "ping2",
    },
)
for srvid in range(10, 10 + 5):
    t.tpcall(
        ".TMIB",
        {
            "TA_CLASS": "T_SERVER",
            "TA_OPERATION": "SET",
            "TA_STATE": "ACT",
            "TA_SRVGRP": "GROUP2",
            "TA_SRVID": srvid,
        },
    )


for srvid in range(1, 1 + 2):
    t.tpcall(
        ".TMIB",
        {
            "TA_CLASS": "T_SERVER",
            "TA_OPERATION": "SET",
            "TA_STATE": "INA",
            "TA_SRVGRP": "GROUP1",
            "TA_SRVID": srvid,
        },
    )
t.tpcall(
    ".TMIB",
    {
        "TA_CLASS": "T_SERVER",
        "TA_OPERATION": "SET",
        "TA_STATE": "INV",
        "TA_SRVGRP": "GROUP1",
        "TA_SRVID": 1,
    },
)
t.tpcall(
    ".TMIB",
    {
        "TA_CLASS": "T_GROUP",
        "TA_OPERATION": "SET",
        "TA_STATE": "INA",
        "TA_SRVGRP": "GROUP1",
    },
)
t.tpcall(
    ".TMIB",
    {
        "TA_CLASS": "T_GROUP",
        "TA_OPERATION": "SET",
        "TA_STATE": "INV",
        "TA_SRVGRP": "GROUP1",
    },
)
