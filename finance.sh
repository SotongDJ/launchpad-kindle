#!/bin/sh
installdir=/mnt/us/SotongDJ
pythonbin=/mnt/us/python/bin/python2.6
nowdate=`date +%Y%m%d`
finatemp=/mnt/us/SotongDJ/finatemp
finance=/mnt/us/DK_Documents/Finance

case "$1" in
    copy)
		ls -1 $finance > $finatemp
		$pythonbin "$installdir/finance.py" $nowdate
    *)
        echo "Usage: $0 {copy}"
        exit 1
        ;;
esac

exit 0
