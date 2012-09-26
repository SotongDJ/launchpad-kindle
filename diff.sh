#!/bin/sh
## echo 7, ## 4, read 1, diff 15, rm 2, gedit 1
echo ============================================
echo "compare scripts (between kindle and com.)"
echo --------------------------------------------
echo "\n----------gensl.py">>/tmp/difftemp
diff /media/Kindle/SotongDJ/gensl.py ~/github/launchpad-kindle/gensl.py >> /tmp/difftemp
echo "\n----------genpl.py">>/tmp/difftemp
diff /media/Kindle/SotongDJ/genpl.py ~/github/launchpad-kindle/genpl.py >> /tmp/difftemp
echo "\n----------config.py">>/tmp/difftemp
diff /media/Kindle/SotongDJ/config.py ~/github/launchpad-kindle/config.py >> /tmp/difftemp
echo "\n----------finance.sh">>/tmp/difftemp
diff /media/Kindle/SotongDJ/finance.sh ~/github/launchpad-kindle/finance.sh >> /tmp/difftemp
echo "\n----------finance.py">>/tmp/difftemp
diff /media/Kindle/SotongDJ/finance.py ~/github/launchpad-kindle/finance.py >> /tmp/difftemp
echo "\n----------file.sh">>/tmp/difftemp
diff /media/Kindle/SotongDJ/file.sh ~/github/launchpad-kindle/file.sh >> /tmp/difftemp
echo "\n----------fm.py">>/tmp/difftemp
diff /media/Kindle/SotongDJ/fm.py ~/github/launchpad-kindle/fm.py >> /tmp/difftemp
echo "\n----------tree.py">>/tmp/difftemp
diff /media/Kindle/SotongDJ/tree.py ~/github/launchpad-kindle/tree.py >> /tmp/difftemp
echo "\n----------screen.py">>/tmp/difftemp
diff /media/Kindle/SotongDJ/screen.py ~/github/launchpad-kindle/screen.py >> /tmp/difftemp
echo "\n----------record.sh">>/tmp/difftemp
diff /media/Kindle/SotongDJ/record.sh ~/github/launchpad-kindle/record.sh >> /tmp/difftemp
echo "\n----------system.py">>/tmp/difftemp
diff /media/Kindle/SotongDJ/system.py ~/github/launchpad-kindle/system.py >> /tmp/difftemp
echo "\n----------test.sh">>/tmp/difftemp
diff /media/Kindle/SotongDJ/test.sh ~/github/launchpad-kindle/test.sh >> /tmp/difftemp
echo "\n----------python.py">>/tmp/difftemp
diff /media/Kindle/SotongDJ/python.py ~/github/launchpad-kindle/python.py >> /tmp/difftemp
##
echo "\n----------SotongDJ.ini">>/tmp/difftemp
diff /media/Kindle/launchpad/SotongDJ.ini ~/github/launchpad-kindle/launchpad/SotongDJ.ini >> /tmp/difftemp
echo "\n----------mplayer.ini">>/tmp/difftemp
diff /media/Kindle/launchpad/mplayer.ini ~/github/launchpad-kindle/launchpad/mplayer.ini >> /tmp/difftemp
echo "\n----------servicecmds.ini">>/tmp/difftemp
diff /media/Kindle/launchpad/servicecmds.ini ~/github/launchpad-kindle/launchpad/servicecmds.ini >> /tmp/difftemp
##
echo "\n----------control.sh">>/tmp/difftemp
diff /media/Kindle/mplayer/control.sh ~/github/launchpad-kindle/mplayer/control.sh >> /tmp/difftemp
gedit /tmp/difftemp
echo "Press any key to continue the process"
read null
rm /tmp/difftemp
echo --------------------------------------------
echo remove temp files
rm -f /media/Kindle/SotongDJ/*temp
echo ============================================
