#!/bin/sh
## echo 12, ## 5, sh 1, read 1, cp 20, rm 2, cat 1
echo ============================================
echo "copy scripts (copy file from com. to kindle)"
echo --------------------------------------------
echo "Make sure you know what are you doing."
echo --------------------------------------------
echo "diff record(s):"
sh ~/github/launchpad-kindle/diff.sh
echo --------------------------------------------
echo "Press any key to start the process"
read null
echo --------------------------------------------
cp -v -u ~/github/launchpad-kindle/gensl.py /media/Kindle/SotongDJ/gensl.py >> /tmp/pushtemp
cp -v -u ~/github/launchpad-kindle/genpl.py /media/Kindle/SotongDJ/genpl.py >> /tmp/pushtemp
cp -v -u ~/github/launchpad-kindle/config.py /media/Kindle/SotongDJ/config.py >> /tmp/pushtemp
cp -v -u ~/github/launchpad-kindle/finance.sh /media/Kindle/SotongDJ/finance.sh >> /tmp/pushtemp
cp -v -u ~/github/launchpad-kindle/finance.py /media/Kindle/SotongDJ/finance.py >> /tmp/pushtemp
cp -v -u ~/github/launchpad-kindle/file.sh /media/Kindle/SotongDJ/file.sh >> /tmp/pushtemp
cp -v -u ~/github/launchpad-kindle/fm.py /media/Kindle/SotongDJ/fm.py >> /tmp/pushtemp
cp -v -u ~/github/launchpad-kindle/tree.py /media/Kindle/SotongDJ/tree.py >> /tmp/pushtemp
cp -v -u ~/github/launchpad-kindle/screen.py /media/Kindle/SotongDJ/screen.py >> /tmp/pushtemp
cp -v -u ~/github/launchpad-kindle/record.sh /media/Kindle/SotongDJ/record.sh >> /tmp/pushtemp
cp -v -u ~/github/launchpad-kindle/system.py /media/Kindle/SotongDJ/system.py >> /tmp/pushtemp
cp -v -u ~/github/launchpad-kindle/test.sh /media/Kindle/SotongDJ/test.sh >> /tmp/pushtemp
cp -v -u ~/github/launchpad-kindle/python.py /media/Kindle/SotongDJ/python.py >> /tmp/pushtemp
##
cp -v -u ~/github/launchpad-kindle/changelog /media/Kindle/documents/00-self/KINDLE/"01a-Changelog.txt" >> /tmp/pushtemp
cp -v -u ~/github/launchpad-kindle/man /media/Kindle/documents/00-self/KINDLE/"01b-Manual of launchpad-kindle.txt" >> /tmp/pushtemp
cp -v -u ~/github/launchpad-kindle/SCL /media/Kindle/documents/00-self/KINDLE/"01a-Summary of ChangeLog.txt" >> /tmp/pushtemp
##
cp -v -u ~/github/launchpad-kindle/launchpad/SotongDJ.ini /media/Kindle/launchpad/SotongDJ.ini >> /tmp/pushtemp
cp -v -u ~/github/launchpad-kindle/launchpad/mplayer.ini /media/Kindle/launchpad/mplayer.ini >> /tmp/pushtemp
cp -v -u ~/github/launchpad-kindle/launchpad/servicecmds.ini /media/Kindle/launchpad/servicecmds.ini >> /tmp/pushtemp
##
cp -v -u ~/github/launchpad-kindle/mplayer/control.sh /media/Kindle/mplayer/control.sh >> /tmp/pushtemp
cat /tmp/pushtemp |more
rm /tmp/pushtemp
echo --------------------------------------------
echo remove temp files
rm -f /media/Kindle/SotongDJ/*temp
echo ============================================
