import sys
import tuxedo as t

req = t.Fextread32(sys.stdin)
_, _, res = t.tpcall(req["SRVCNM"][0], req)
t.Ffprint32(res, sys.stdout)
