import tuxedo as t

for _ in range(100):
    _, _, res = t.tpcall("TOUPPER", "Hello, world!")
    print(res)
