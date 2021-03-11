import tuxedo as t

fieldid = t.Fldid32("TA_CLASS")
assert t.Fname32(fieldid) == "TA_CLASS"
assert t.Fldtype32(fieldid) == t.FLD_STRING
assert t.Fldno32(fieldid) == 6000 + 2
assert t.Fmkfldid32(t.FLD_STRING, 6000 + 2) == fieldid
