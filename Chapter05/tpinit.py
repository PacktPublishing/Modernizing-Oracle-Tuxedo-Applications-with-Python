import tuxedo as t

t.tpinit(
    usrname=None,
    cltname="tpsysadm",
    passwd=None,
    grpname=None,
    flags=t.TPMULTICONTEXTS,
)
print(t.tpcall("PING_1", {}).data)
t.tpterm()
