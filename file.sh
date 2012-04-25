#!/bin/sh
## -----------Change it if different---------
pythonbin=/mnt/us/python/bin/python
mainlog=/mnt/us/documents/00-self/Log.txt
backuplog=/mnt/us/documents/00-self/bkLog

freedownload=/mnt/us/freedownload/freedownload.log
launchpad=/mnt/us/launchpad/launchpad.log

systempy=/mnt/us/SotongDJ/system.py
dkconfig=/mnt/us/DK_System/xKindle/config.ini
dkconfbk=/mnt/us/DK_System/xKindle/configbk
## ----------------------------------------------
case "$1" in
    copy)
		cp -v -u /mnt/us/SotongDJ/createlist.py /mnt/us/documents/00-self/KINDLE/createlist-py.txt
		cp -v -u /mnt/us/SotongDJ/createlist.sh /mnt/us/documents/00-self/KINDLE/createlist-sh.txt
		cp -v -u /mnt/us/SotongDJ/gensl.py /mnt/us/documents/00-self/KINDLE/gensl-py.txt
		cp -v -u /mnt/us/SotongDJ/genpl.py /mnt/us/documents/00-self/KINDLE/genpl-py.txt
		cp -v -u /mnt/us/SotongDJ/finance.sh /mnt/us/documents/00-self/KINDLE/finance-sh.txt
		cp -v -u /mnt/us/SotongDJ/finance.py /mnt/us/documents/00-self/KINDLE/finance-py.txt
		cp -v -u /mnt/us/SotongDJ/filter.py /mnt/us/documents/00-self/KINDLE/filter-py.txt
		cp -v -u /mnt/us/SotongDJ/file.sh /mnt/us/documents/00-self/KINDLE/file-sh.txt
		cp -v -u /mnt/us/SotongDJ/fm.py /mnt/us/documents/00-self/KINDLE/fm-py.txt
		cp -v -u /mnt/us/SotongDJ/tree.py /mnt/us/documents/00-self/KINDLE/tree-py.txt
		cp -v -u /mnt/us/SotongDJ/split.py /mnt/us/documents/00-self/KINDLE/split-py.txt
		cp -v -u /mnt/us/SotongDJ/screen.py /mnt/us/documents/00-self/KINDLE/screen-py.txt
		cp -v -u /mnt/us/SotongDJ/record.sh /mnt/us/documents/00-self/KINDLE/record-sh.txt
		cp -v -u /mnt/us/SotongDJ/system.py /mnt/us/documents/00-self/KINDLE/system-py.txt
		cp -v -u /mnt/us/SotongDJ/test.sh /mnt/us/documents/00-self/KINDLE/test-sh.txt
		cp -v -u /mnt/us/SotongDJ/python.py /mnt/us/documents/00-self/KINDLE/python-py.txt
		cp -v -u /mnt/us/launchpad/SotongDJ.ini /mnt/us/documents/00-self/KINDLE/launchpad-SotongDJ-ini.txt
		cp -v -u /mnt/us/launchpad/mplayer.ini /mnt/us/documents/00-self/KINDLE/launchpad-mplayer-ini.txt
		cp -v -u /mnt/us/mplayer/control.sh /mnt/us/documents/00-self/KINDLE/mplayer-control-sh.txt
        ;;
    boot2kindle)
        cp $dkconfig $dkconfbk
        rm $dkconfig
        $pythonbin $systempy kindle
        ;;
    boot2duokan)
        cp $dkconfig $dkconfbk
        rm $dkconfig
        $pythonbin $systempy duokan
        ;;
    ch2duokan)
        ##still in experimental 
##        killall -9 ebook
##        killall -9 KindleApp
##        killall -9 UsbSignal.bin
##        /etc/init.d/framework stop
##        /mnt/us/DK_System/rundk.sh lite
        ;;
    keystore)
        mntroot rw
        cp /mnt/us/SotongDJ/developer.keystore /var/local/java/keystore/developer.keystore
        mntroot ro
        ;;
    *)
        echo "Usage: $0 {copy|sync|boot2kindle|boot2duokan}"
        exit 1
        ;;
esac

exit 0
