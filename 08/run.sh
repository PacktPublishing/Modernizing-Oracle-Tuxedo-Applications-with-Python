export PATH=$TUXDIR/bin:$PATH
export LD_LIBRARY_PATH=$TUXDIR/lib:$LD_LIBRARY_PATH
export TUXCONFIG=`pwd`/tuxconfig
export FLDTBLDIR32=$TUXDIR/udataobj:`pwd`
export FIELDTBLS32=Usysfl32,tpadm,example

cat ubbconfig.in \
| sed s:@TUXDIR@:$TUXDIR:g \
| sed s:@UNAME@:`uname -n`:g \
| sed s:@CURDIR@:`pwd`:g > ubbconfig

export QMCONFIG=`pwd`/qmconfig
echo "crdl $QMCONFIG 0 200" | qmadmin 
echo "qspc QSPACE 230999 100 3 5 5 100 ERR y 16" | qmadmin
echo -e "qopen QSPACE\nqcr ERR time none 0 0 100% 0% ''" | qmadmin 
echo -e "qopen QSPACE\nqcr REQ time none 3 5 100% 0% ''" | qmadmin 
echo -e "qopen QSPACE\nqcr RES time none 3 5 100% 0% ''" | qmadmin 

tmipcrm -y
tmloadcf -y ubbconfig
rm tlog
echo crdl -z `pwd`/tlog -b 200 | tmadmin
echo crlog -m tuxapp | tmadmin

tmboot -y
bash
tmshutdown -y
