import tuxedo as t

print(t.tpcall("GETRATES", {}).data)

t.tpcall("GETRATES_ASYNC", {})
