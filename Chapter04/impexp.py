import tuxedo as t

print(t.tpexport("Hello, world!"))
print(t.tpexport({"TA_CLASS": "Hello, world!"}))
print(t.tpexport({"TA_CLASS": "Hello, world!"}, t.TPEX_STRING))
print(t.tpimport(t.tpexport({"TA_CLASS": "Hello, world!"})))
print(
    t.tpimport(
        t.tpexport({"TA_CLASS": "Hello, world!"}, t.TPEX_STRING),
        t.TPEX_STRING,
    )
)
