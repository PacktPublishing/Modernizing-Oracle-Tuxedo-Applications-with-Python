export PATH=$TUXDIR/bin:$PATH
export LD_LIBRARY_PATH=$TUXDIR/lib:$LD_LIBRARY_PATH
export TUXCONFIG=`pwd`/tuxconfig
export FLDTBLDIR32=$TUXDIR/udataobj:`pwd`
export FIELDTBLS32=Usysfl32,tpadm,example

#sudo yum -y install oracle-instantclient19.9-basic
#sudo yum -y install oracle-instantclient19.9-devel
#sudo yum -y install oracle-instantclient19.9-sqlplus

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
bash
tmshutdown -y
