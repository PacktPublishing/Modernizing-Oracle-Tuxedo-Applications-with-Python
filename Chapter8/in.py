import tuxedo as t

qctl = t.tpenqueue(
    "QSPACE",
    "REQ",
    t.TPQCTL(
        corrid="8",
        replyqueue="RES",
        flags=t.TPQCORRID + t.TPQREPLYQ,
    ),
    {"TA_STATUS": "do"},
)

qctl, data = t.tpdequeue(
    "QSPACE",
    "RES",
    t.TPQCTL(corrid="8", flags=t.TPQGETBYCORRID + t.TPQWAIT),
)
print(data)
