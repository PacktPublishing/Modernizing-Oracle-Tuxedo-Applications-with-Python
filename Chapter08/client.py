import tuxedo as t

qctl = t.tpenqueue(
    "QSPACE", "ERR", t.TPQCTL(), {"TA_STATUS": "Hello /Q!"}
)
print(qctl.flags)
qctl, data = t.tpdequeue("QSPACE", "ERR", t.TPQCTL())
print(qctl.flags, data)

q = t.tpenqueue(
    "QSPACE",
    "ERR",
    t.TPQCTL(corrid="hello", flags=t.TPQCORRID + t.TPQMSGID),
    {"TA_STATUS": "Hello!"},
)
print(q.corrid, q.msgid)

q, data = t.tpdequeue(
    "QSPACE",
    "ERR",
    t.TPQCTL(corrid="hello", flags=t.TPQGETBYCORRID),
)
print(q.corrid, data)

q = t.tpenqueue(
    "QSPACE",
    "ERR",
    t.TPQCTL(deq_time=60, flags=t.TPQTIME_REL),
    {"TA_STATUS": "Delayed hello!"},
)

try:
    qctl, data = t.tpdequeue("QSPACE", "ERR", t.TPQCTL())
except:
    pass

import time

time.sleep(60)

qctl, data = t.tpdequeue("QSPACE", "ERR", t.TPQCTL())
