export PATH=$TUXDIR/bin:$PATH
export LD_LIBRARY_PATH=$TUXDIR/lib:$LD_LIBRARY_PATH
export TUXCONFIG=`pwd`/tuxconfig
export FLDTBLDIR32=$TUXDIR/udataobj:`pwd`
export FIELDTBLS32=Usysfl32,tpadm,example

tmipcrm -y
rm -f $TUXCONFIG
python3 tpadmcall.py
cp ping1.py ping.py
tmboot -y
#bash
# mv ping.py ping.old; cp ping2.py ping.py; tmshutdown -i 1; tmboot -i 1; tmshutdown -i 2; tmboot -i 2
tmshutdown -y
