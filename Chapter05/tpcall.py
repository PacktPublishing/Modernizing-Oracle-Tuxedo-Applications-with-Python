import tuxedo as t

rval, rcode, data = t.tpcall("PING_1", {})
print(rval, rcode, data)

r = t.tpcall("PING_1", {})
print(r.rval, r.rcode, r.data, r.cd)

try:
    t.tpcall("DOES_NOT_EXIST", {})
except t.XatmiException as e:
    print(e, e.code)
