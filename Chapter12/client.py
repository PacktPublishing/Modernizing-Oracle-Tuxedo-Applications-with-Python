import tuxedo as t

print(t.tpcall("TUX1", {}).data)
print(t.tpcall("NATS1", {}).data)
print(t.tpcall("TUX2", {}).data)
print(t.tpcall("NATS2", {}).data)
