export PATH=$TUXDIR/bin:$PATH
export LD_LIBRARY_PATH=$TUXDIR/lib:$LD_LIBRARY_PATH
export TUXCONFIG=`pwd`/tuxconfig
export FLDTBLDIR32=$TUXDIR/udataobj:`pwd`
export FIELDTBLS32=Usysfl32,tpadm,example

cat ubbconfig.in \
| sed s:@TUXDIR@:$TUXDIR:g \
| sed s:@UNAME@:`uname -n`:g \
| sed s:@CURDIR@:`pwd`:g > ubbconfig

tmipcrm -y
tmloadcf -y ubbconfig
rm tlog
echo crdl -z `pwd`/tlog -b 200 | tmadmin
echo crlog -m tuxapp | tmadmin
tmboot -y
echo -e "SRVCNM\t.TMIB\n" | ud32 -t 10
bash
tmshutdown -y
