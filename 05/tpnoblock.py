import tuxedo as t

cd = t.tpacall("PING_1", {})
while True:
    print("Waiting for a response")
    try:
        _, _, res = t.tpgetrply(cd, t.TPNOBLOCK)
        break
    except t.XatmiException as e:
        if e.code == t.TPEBLOCK:
            continue
        raise
