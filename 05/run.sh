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
echo -e "SRVCNM\tUNADVERTISED\n" | ud32
echo -e "SRVCNM\tPING_1\n" | ud32
echo -e "SRVCNM\tPING_2\n" | ud32
echo -e "SRVCNM\tPING_1\n\n\n\n" | ud32
echo -e "SRVCNM\tWORK\n" | ud32
tmshutdown -y
