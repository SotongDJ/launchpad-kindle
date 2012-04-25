#!/bin/sh
## echo 12, ## 5, sh 1, read 1, cp 22, rm 2, cat 1
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
cp -v -u ~/github/launchpad-kindle/createlist.py /media/Kindle/SotongDJ/createlist.py > /tmp/difftemp
cp -v -u ~/github/launchpad-kindle/createlist.sh /media/Kindle/SotongDJ/createlist.sh >> /tmp/difftemp
cp -v -u ~/github/launchpad-kindle/gensl.py /media/Kindle/SotongDJ/gensl.py >> /tmp/difftemp
cp -v -u ~/github/launchpad-kindle/genpl.py /media/Kindle/SotongDJ/genpl.py >> /tmp/difftemp
cp -v -u ~/github/launchpad-kindle/finance.sh /media/Kindle/SotongDJ/finance.sh >> /tmp/difftemp
cp -v -u ~/github/launchpad-kindle/finance.py /media/Kindle/SotongDJ/finance.py >> /tmp/difftemp
cp -v -u ~/github/launchpad-kindle/filter.py /media/Kindle/SotongDJ/filter.py >> /tmp/difftemp
cp -v -u ~/github/launchpad-kindle/file.sh /media/Kindle/SotongDJ/file.sh >> /tmp/difftemp
cp -v -u ~/github/launchpad-kindle/fm.py /media/Kindle/SotongDJ/fm.py >> /tmp/difftemp
cp -v -u ~/github/launchpad-kindle/tree.py /media/Kindle/SotongDJ/tree.py >> /tmp/difftemp
cp -v -u ~/github/launchpad-kindle/split.py /media/Kindle/SotongDJ/split.py >> /tmp/difftemp
cp -v -u ~/github/launchpad-kindle/screen.py /media/Kindle/SotongDJ/screen.py >> /tmp/difftemp
cp -v -u ~/github/launchpad-kindle/record.sh /media/Kindle/SotongDJ/record.sh >> /tmp/difftemp
cp -v -u ~/github/launchpad-kindle/system.py /media/Kindle/SotongDJ/system.py >> /tmp/difftemp
cp -v -u ~/github/launchpad-kindle/test.sh /media/Kindle/SotongDJ/test.sh >> /tmp/difftemp
cp -v -u ~/github/launchpad-kindle/python.py /media/Kindle/SotongDJ/python.py >> /tmp/difftemp
##
cp -v -u ~/github/launchpad-kindle/changelog /media/Kindle/documents/00-self/KINDLE/"Changelog.txt" >> /tmp/difftemp
cp -v -u ~/github/launchpad-kindle/man /media/Kindle/documents/00-self/KINDLE/"Manual of launchpad-kindle.txt" >> /tmp/difftemp
cp -v -u ~/github/launchpad-kindle/SCL /media/Kindle/documents/00-self/KINDLE/"Summary of ChangeLog.txt" >> /tmp/difftemp
##
cp -v -u ~/github/launchpad-kindle/launchpad/SotongDJ.ini /media/Kindle/launchpad/SotongDJ.ini >> /tmp/difftemp
cp -v -u ~/github/launchpad-kindle/launchpad/mplayer.ini /media/Kindle/launchpad/mplayer.ini >> /tmp/difftemp
##
cp -v -u ~/github/launchpad-kindle/mplayer/control.sh /media/Kindle/mplayer/control.sh >> /tmp/difftemp
cat /tmp/difftemp |more
rm /tmp/difftemp
echo --------------------------------------------
echo remove temp files
rm -f /media/Kindle/SotongDJ/*temp
echo ============================================
