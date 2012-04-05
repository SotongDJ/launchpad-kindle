#!/bin/sh
## -----------Change it if different---------
pythonbin=/mnt/us/python/bin/python
mainlog=/mnt/us/documents/00-self/Log.txt
backuplog=/mnt/us/documents/00-self/bkLog

freedownload=/mnt/us/freedownload/freedownload.log
launchpad=/mnt/us/launchpad/launchpad.log

notesto=/mnt/us/DK_Documents/Notes-ReadOnly
notesfrom=`cat /mnt/us/SotongDJ/protect`

systempy=/mnt/us/SotongDJ/system.py
dkconfig=/mnt/us/DK_System/xKindle/config.ini
dkconfbk=/mnt/us/DK_System/xKindle/configbk
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
	cplp)
		## Please edit this case on computer, dont change it under Kindle
		cp -t "$notesfrom" createlist.py createlist.sh file.sh filter.py finance.py finance.sh record.sh system.py
		cp -t "$launchpaddir" mplayer.ini SotongDJ.ini servicecmds.ini
		;;
    cleanlp)
		rm -f "$notesfrom"/createlist.py "$notesfrom"/createlist.sh "$notesfrom"/file.sh "$notesfrom"/filter.py "$notesfrom"/finance.py "$notesfrom"/finance.sh "$notesfrom"/record.sh "$notesfrom"/system.py "$launchpaddir"/mplayer.ini "$launchpaddir"/SotongDJ.ini "$launchpaddir"/servicecmds.ini
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
