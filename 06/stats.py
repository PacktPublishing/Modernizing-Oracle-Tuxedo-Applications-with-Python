import tuxedo as t

t.tpinit(cltname="tpsysop")
machine = t.tpadmcall(
    {
        "TA_CLASS": "T_MACHINE",
        "TA_OPERATION": "GET",
        "TA_FLAGS": t.MIB_LOCAL,
    }
).data
print("Timestamp:", machine["TA_CURTIME"][0])
print("Service calls:", machine["TA_NUMREQ"][0])
print("Transactions started:", machine["TA_NUMTRAN"][0])
print("Transactions aborted:", machine["TA_NUMTRANABT"][0])
print("Transactions committed:", machine["TA_NUMTRANCMT"][0])
