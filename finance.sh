#!/bin/sh
## -----------Change it if different---------
installdir=/mnt/us/SotongDJ
pythonbin=/mnt/us/python/bin/python2.6
nowdate=`date +%Y%m%d`
finatemp=/mnt/us/SotongDJ/finatemp
finance=`cat /mnt/us/SotongDJ/protect`
## --------DeBug Usage----------------------
#pythonbin=python
## ----------------------------------------------

case "$1" in
    copy)
		ls -1 $finance > $finatemp
		$pythonbin "$installdir/finance.py" $nowdate
		echo shell script run>"$installdir/$nowdate.debug"
		;;
    *)
        echo "Usage: $0 {copy}"
        exit 1
        ;;
esac

exit 0
