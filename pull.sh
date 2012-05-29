#!/bin/sh
## echo 12, ## 4, sh 1, read 1, cp 17, rm 2, cat 1
echo ============================================
echo "copy scripts (copy file from kindle to com.)"
echo --------------------------------------------
echo "Make sure you know what are you doing."
echo --------------------------------------------
echo "diff record(s):"
sh ~/github/launchpad-kindle/diff.sh
echo --------------------------------------------
echo "Press any key to start the process"
read null
echo --------------------------------------------
cp -v -u /media/Kindle/SotongDJ/gensl.py ~/github/launchpad-kindle/gensl.py >> /tmp/pulltemp
cp -v -u /media/Kindle/SotongDJ/genpl.py ~/github/launchpad-kindle/genpl.py >> /tmp/pulltemp
cp -v -u /media/Kindle/SotongDJ/config.py ~/github/launchpad-kindle/config.py >> /tmp/pulltemp
cp -v -u /media/Kindle/SotongDJ/finance.sh ~/github/launchpad-kindle/finance.sh >> /tmp/pulltemp
cp -v -u /media/Kindle/SotongDJ/finance.py ~/github/launchpad-kindle/finance.py >> /tmp/pulltemp
cp -v -u /media/Kindle/SotongDJ/file.sh ~/github/launchpad-kindle/file.sh >> /tmp/pulltemp
cp -v -u /media/Kindle/SotongDJ/fm.py ~/github/launchpad-kindle/fm.py >> /tmp/pulltemp
cp -v -u /media/Kindle/SotongDJ/tree.py ~/github/launchpad-kindle/tree.py >> /tmp/pulltemp
cp -v -u /media/Kindle/SotongDJ/screen.py ~/github/launchpad-kindle/screen.py >> /tmp/pulltemp
cp -v -u /media/Kindle/SotongDJ/record.sh ~/github/launchpad-kindle/record.sh >> /tmp/pulltemp
cp -v -u /media/Kindle/SotongDJ/system.py ~/github/launchpad-kindle/system.py >> /tmp/pulltemp
cp -v -u /media/Kindle/SotongDJ/test.sh ~/github/launchpad-kindle/test.sh >> /tmp/pulltemp
cp -v -u /media/Kindle/SotongDJ/python.py ~/github/launchpad-kindle/python.py >> /tmp/pulltemp
##
cp -v -u /media/Kindle/launchpad/SotongDJ.ini ~/github/launchpad-kindle/launchpad/SotongDJ.ini >> /tmp/pulltemp
cp -v -u /media/Kindle/launchpad/mplayer.ini ~/github/launchpad-kindle/launchpad/mplayer.ini >> /tmp/pulltemp
##
cp -v -u /media/Kindle/mplayer/control.sh ~/github/launchpad-kindle/mplayer/control.sh >> /tmp/pulltemp
cat /tmp/pulltemp |more
rm /tmp/pulltemp
echo --------------------------------------------
echo remove temp files
rm -f /media/Kindle/SotongDJ/*temp
echo ============================================
