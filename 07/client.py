import tuxedo as t

print("In transaction?", t.tpgetlev())
t.tpbegin(3)
print("In transaction?", t.tpgetlev())
# t.tpcall("PING", {}, t.TPNOTRAN)
trxid = t.tpsuspend()
print("In transaction?", t.tpgetlev())
t.tpcall("PING", {})
print("In transaction?", t.tpgetlev())
print(trxid)
print("In transaction?", t.tpgetlev())
t.tpresume(trxid)
print("In transaction?", t.tpgetlev())
t.tpcommit()
print("In transaction?", t.tpgetlev())