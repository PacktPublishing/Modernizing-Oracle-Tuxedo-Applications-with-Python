import tuxedo as t

calls = []
calls.append(t.tpacall("PING_1", {}))
calls.append(t.tpacall("PING_2", {}))

while calls:
    r = t.tpgetrply(-1, t.TPGETANY)
    calls.remove(r.cd)
    print(r.data)
