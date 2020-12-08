import tuxedo as t

_, _, res = t.tpcall("TOUPPER", "Hello, world!")
print(res)
