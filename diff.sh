#!/bin/sh
echo ============================================
echo "compare scripts (between kindle and com.)"
echo --------------------------------------------
diff /media/Kindle/SotongDJ/createlist.py ~/github/launchpad-kindle/createlist.py
diff /media/Kindle/SotongDJ/createlist.sh ~/github/launchpad-kindle/createlist.sh
diff /media/Kindle/SotongDJ/finance.sh ~/github/launchpad-kindle/finance.sh
diff /media/Kindle/SotongDJ/finance.py ~/github/launchpad-kindle/finance.py
diff /media/Kindle/SotongDJ/filter.py ~/github/launchpad-kindle/filter.py
diff /media/Kindle/SotongDJ/file.sh ~/github/launchpad-kindle/file.sh
diff /media/Kindle/SotongDJ/fm.py ~/github/launchpad-kindle/fm.py
diff /media/Kindle/SotongDJ/tree.py ~/github/launchpad-kindle/tree.py
diff /media/Kindle/SotongDJ/split.py ~/github/launchpad-kindle/split.py
diff /media/Kindle/SotongDJ/screen.py ~/github/launchpad-kindle/screen.py
diff /media/Kindle/SotongDJ/record.sh ~/github/launchpad-kindle/record.sh
diff /media/Kindle/SotongDJ/system.py ~/github/launchpad-kindle/system.py
diff /media/Kindle/SotongDJ/test.sh ~/github/launchpad-kindle/test.sh
diff /media/Kindle/SotongDJ/python.py ~/github/launchpad-kindle/python.py
diff /media/Kindle/SotongDJ/changelog.txt ~/github/launchpad-kindle/changelog
diff /media/Kindle/launchpad/SotongDJ.ini ~/github/launchpad-kindle/launchpad/SotongDJ.ini
diff /media/Kindle/launchpad/mplayer.ini ~/github/launchpad-kindle/launchpad/mplayer.ini
diff /media/Kindle/mplayer/control.sh ~/github/launchpad-kindle/mplayer/control.sh
echo --------------------------------------------
echo remove temp files
rm -f /media/Kindle/SotongDJ/*temp
echo ============================================
