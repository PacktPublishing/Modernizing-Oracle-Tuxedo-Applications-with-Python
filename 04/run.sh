export PATH=$TUXDIR/bin:$PATH
export LD_LIBRARY_PATH=$TUXDIR/lib:$LD_LIBRARY_PATH
export TUXCONFIG=`pwd`/tuxconfig
export FLDTBLDIR32=$TUXDIR/udataobj:`pwd`
export FIELDTBLS32=Usysfl32,tpadm,example

cat ubbconfig.in \
| sed s:@TUXDIR@:$TUXDIR:g \
| sed s:@UNAME@:`uname -n`:g \
| sed s:@CURDIR@:`pwd`:g > ubbconfig

tmloadcf -y ubbconfig
tmboot -y
echo -e "SRVCNM\t.TMIB\nTA_CLASS\tT_DOMAIN\nTA_OPERATION\tGET\n\n" | ud32
echo -e "SRVCNM\t.TMIB\nTA_CLASS\tT_DOMAIN\nTA_OPERATION\tGET\n\n" | python3 ud32.py
python3 client.py
python3 ta_class.py
python3 impexp.py
python3 boolexpr.py
python3 fml32.py  
tmshutdown -y
