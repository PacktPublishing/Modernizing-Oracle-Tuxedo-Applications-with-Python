import tuxedo as t

_, _, res = t.tpcall(
    ".TMIB",
    {
        "PARAM": [
            {
                "NAME": "user",
                "VALUE": "oracle",
            },
            {
                "NAME": "password",
            },
        ]
    },
)
print(res)

assert t.Fldid32("SAMENAME") == t.Fldid32("SAMEID")
assert t.Fname32(t.Fldid32("SAMEID")) == "SAMENAME"
_, _, res = t.tpcall(".TMIB", {"SAMEID": "ID"})
print(res)

t.tpcall(".TMIB", {"THERE_IS_NO_SUCH_FIELD": "?"})
