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

tmboot -y
bash
tmshutdown -y
