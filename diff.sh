#!/bin/sh
## echo 6, ## 5, sh 1, read 1, diff 19, rm 2, cat 1
echo ============================================
echo "compare scripts (between kindle and com.)"
echo --------------------------------------------
diff /media/Kindle/SotongDJ/createlist.py ~/github/launchpad-kindle/createlist.py > /tmp/difftemp
diff /media/Kindle/SotongDJ/createlist.sh ~/github/launchpad-kindle/createlist.sh >> /tmp/difftemp
diff /media/Kindle/SotongDJ/gensl.py ~/github/launchpad-kindle/gensl.py >> /tmp/difftemp
diff /media/Kindle/SotongDJ/genpl.py ~/github/launchpad-kindle/genpl.py >> /tmp/difftemp
diff /media/Kindle/SotongDJ/finance.sh ~/github/launchpad-kindle/finance.sh >> /tmp/difftemp
diff /media/Kindle/SotongDJ/finance.py ~/github/launchpad-kindle/finance.py >> /tmp/difftemp
diff /media/Kindle/SotongDJ/filter.py ~/github/launchpad-kindle/filter.py >> /tmp/difftemp
diff /media/Kindle/SotongDJ/file.sh ~/github/launchpad-kindle/file.sh >> /tmp/difftemp
diff /media/Kindle/SotongDJ/fm.py ~/github/launchpad-kindle/fm.py >> /tmp/difftemp
diff /media/Kindle/SotongDJ/tree.py ~/github/launchpad-kindle/tree.py >> /tmp/difftemp
diff /media/Kindle/SotongDJ/split.py ~/github/launchpad-kindle/split.py >> /tmp/difftemp
diff /media/Kindle/SotongDJ/screen.py ~/github/launchpad-kindle/screen.py >> /tmp/difftemp
diff /media/Kindle/SotongDJ/record.sh ~/github/launchpad-kindle/record.sh >> /tmp/difftemp
diff /media/Kindle/SotongDJ/system.py ~/github/launchpad-kindle/system.py >> /tmp/difftemp
diff /media/Kindle/SotongDJ/test.sh ~/github/launchpad-kindle/test.sh >> /tmp/difftemp
diff /media/Kindle/SotongDJ/python.py ~/github/launchpad-kindle/python.py >> /tmp/difftemp
##
diff /media/Kindle/launchpad/SotongDJ.ini ~/github/launchpad-kindle/launchpad/SotongDJ.ini >> /tmp/difftemp
diff /media/Kindle/launchpad/mplayer.ini ~/github/launchpad-kindle/launchpad/mplayer.ini >> /tmp/difftemp
##
diff /media/Kindle/mplayer/control.sh ~/github/launchpad-kindle/mplayer/control.sh >> /tmp/difftemp
cat /tmp/difftemp |more
rm /tmp/difftemp
echo --------------------------------------------
echo remove temp files
rm -f /media/Kindle/SotongDJ/*temp
echo ============================================
