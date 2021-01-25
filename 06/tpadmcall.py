import tuxedo as t

t.tpadmcall(
    {
        "TA_CLASS": "T_DOMAIN",
        "TA_OPERATION": "SET",
        "TA_STATE": "NEW",
        "TA_MASTER": "tuxapp",
        "TA_MODEL": "SHM",
        "TA_IPCKEY": 32769,
    }
)
# Implicit T_MACHINE

t.tpadmcall(
    {
        "TA_CLASS": "T_GROUP",
        "TA_OPERATION": "SET",
        "TA_STATE": "NEW",
        "TA_SRVGRP": "GROUP1",
        "TA_GRPNO": 1,
        "TA_LMID": "tuxapp",
    }
)

t.tpadmcall(
    {
        "TA_CLASS": "T_SERVER",
        "TA_OPERATION": "SET",
        "TA_STATE": "NEW",
        "TA_SRVGRP": "GROUP1",
        "TA_SERVERNAME": "ping.py",
        "TA_SRVID": 1,
        "TA_MIN": 2,
        "TA_MAX": 2,
        "TA_REPLYQ": "Y",
        "TA_MAXGEN": 2,
        "TA_RESTART": "Y",
        "TA_GRACE": 0,
        "TA_RQADDR": "ping",
    }
)
