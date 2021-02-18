import tuxedo as t

_, _, res = t.tpcall("COUNT", {})
print(res)


t.tpbegin(30)
t.tpcall("STORE", {"TA_SOURCE": "Hello"})
print(t.tpcall("COUNT", {}).data)
print(t.tpcall("COUNTXA", {}).data)
t.tpcommit()
print(t.tpcall("COUNT", {}).data)
