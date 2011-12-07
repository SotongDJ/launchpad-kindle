#!/bin/sh
## -----------Change it if different---------
pythonbin=/mnt/us/python/bin/python2.6
mainlog=/mnt/us/documents/00-self/Log.txt
backuplog=/mnt/us/documents/00-self/bkLog

freedownload=/mnt/us/freedownload/freedownload.log
launchpad=/mnt/us/launchpad/launchpad.log

notesto=/mnt/us/DK_Documents/Notes-ReadOnly
notesfrom=/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user

bootconf=/mnt/us/DK_System/Lite/config.ini
editbtconf=/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user/DKSystemConfig.txt

systempy=/mnt/us/SotongDJ/system.py
dkconfig=/mnt/us/DK_System/Lite/config.ini
dkconfbk=/mnt/us/DK_System/Lite/configbk
## --------DeBug Usage----------------------
#pythonbin=python
## ----------------------------------------------
case "$1" in
    copy)
		## ignore this
		echo "  " > $mainlog
		echo "==============" >> $mainlog
		echo "Log Files - ""$nowdate" >> $mainlog
		echo "--------------" >> $mainlog
		echo "$freedownload"": " >> $mainlog
		cat $freedownload >> $mainlog
		echo "--------------" >> $mainlog
		echo "$launchpad"": " >> $mainlog
		cat $launchpad >> $mainlog
		echo "==============" >> $mainlog
		echo "  " >> $mainlog
		echo "==============" >> $backuplog
		echo "  " >> $backuplog
		echo "==============" >> $backuplog
		cat $mainlog >> $backuplog
        ;;
    sync)
		cp "$notesfrom"/* $notesto
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
##		killall -9 ebook
##		killall -9 KindleApp
##		killall -9 UsbSignal.bin
##		/etc/init.d/framework stop
##		/mnt/us/DK_System/rundk.sh lite
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
