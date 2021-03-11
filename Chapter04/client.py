import tuxedo as t

_, _, res = t.tpcall(
    ".TMIB",
    {
        "TA_CLASS": "T_DOMAIN",
        "TA_OPERATION": "GET",
    },
)
print(res)
