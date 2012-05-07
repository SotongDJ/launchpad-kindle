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
		cp /mnt/us/launchpad/SotongDJ.ini /mnt/us/documents/00-self/KINDLE/01c-launchpad-SotongDJ-ini.txt
		cp /mnt/us/SotongDJ/gensl.py /mnt/us/documents/00-self/KINDLE/02a-gensl-py.txt
		cp /mnt/us/SotongDJ/genpl.py /mnt/us/documents/00-self/KINDLE/02a-genpl-py.txt
		cp /mnt/us/SotongDJ/config.py /mnt/us/documents/00-self/KINDLE/02a-config-py.txt
		cp /mnt/us/SotongDJ/record.sh /mnt/us/documents/00-self/KINDLE/02a-record-sh.txt
#		cp /mnt/us/SotongDJ/createlist.py /mnt/us/documents/00-self/KINDLE/02b-createlist-py.txt
#		cp /mnt/us/SotongDJ/createlist.sh /mnt/us/documents/00-self/KINDLE/02b-createlist-sh.txt
#		cp /mnt/us/SotongDJ/split.py /mnt/us/documents/00-self/KINDLE/02b-split-py.txt
#		cp /mnt/us/SotongDJ/filter.py /mnt/us/documents/00-self/KINDLE/02b-filter-py.txt
		cp /mnt/us/launchpad/mplayer.ini /mnt/us/documents/00-self/KINDLE/02c-launchpad-mplayer-ini.txt
		cp /mnt/us/mplayer/control.sh /mnt/us/documents/00-self/KINDLE/02c-mplayer-control-sh.txt
		cp /mnt/us/SotongDJ/finance.sh /mnt/us/documents/00-self/KINDLE/03-finance-sh.txt
		cp /mnt/us/SotongDJ/finance.py /mnt/us/documents/00-self/KINDLE/03-finance-py.txt
		cp /mnt/us/SotongDJ/screen.py /mnt/us/documents/00-self/KINDLE/04-screen-py.txt
		cp /mnt/us/SotongDJ/system.py /mnt/us/documents/00-self/KINDLE/04-system-py.txt
		cp /mnt/us/SotongDJ/file.sh /mnt/us/documents/00-self/KINDLE/04-file-sh.txt
		cp /mnt/us/SotongDJ/fm.py /mnt/us/documents/00-self/KINDLE/09-fm-py.txt
		cp /mnt/us/SotongDJ/tree.py /mnt/us/documents/00-self/KINDLE/09-tree-py.txt
		cp /mnt/us/SotongDJ/test.sh /mnt/us/documents/00-self/KINDLE/10-test-sh.txt
		cp /mnt/us/SotongDJ/python.py /mnt/us/documents/00-self/KINDLE/10-python-py.txt
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
