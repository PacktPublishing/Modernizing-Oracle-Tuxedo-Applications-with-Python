import tuxedo as t

t.tpsblktime(5, t.TPBLK_ALL | t.TPBLK_SECOND)
t.tpcall("SLEEP", {}, t.TPNOTIME)

t.tpsblktime(5, t.TPBLK_ALL | t.TPBLK_SECOND)
t.tpcall("SLEEP", {})

t.tpsblktime(1, t.TPBLK_ALL | t.TPBLK_SECOND)
cd = t.tpacall("SLEEP", {})
t.tpsblktime(5, t.TPBLK_ALL | t.TPBLK_SECOND)
t.tpgetrply(cd)
