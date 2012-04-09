#!/bin/sh
echo ============================================
echo "copy scripts (copy file from kindle to com.)"
echo --------------------------------------------
echo "Make sure you know what are you doing."
echo --------------------------------------------
echo "diff record(s):"
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
echo "Press any key to start the process"
read null
echo --------------------------------------------
cp -v -u /media/Kindle/SotongDJ/createlist.py ~/github/launchpad-kindle/createlist.py
cp -v -u /media/Kindle/SotongDJ/createlist.sh ~/github/launchpad-kindle/createlist.sh
cp -v -u /media/Kindle/SotongDJ/finance.sh ~/github/launchpad-kindle/finance.sh
cp -v -u /media/Kindle/SotongDJ/finance.py ~/github/launchpad-kindle/finance.py
cp -v -u /media/Kindle/SotongDJ/filter.py ~/github/launchpad-kindle/filter.py
cp -v -u /media/Kindle/SotongDJ/file.sh ~/github/launchpad-kindle/file.sh
cp -v -u /media/Kindle/SotongDJ/fm.py ~/github/launchpad-kindle/fm.py
cp -v -u /media/Kindle/SotongDJ/tree.py ~/github/launchpad-kindle/tree.py
cp -v -u /media/Kindle/SotongDJ/split.py ~/github/launchpad-kindle/split.py
cp -v -u /media/Kindle/SotongDJ/screen.py ~/github/launchpad-kindle/screen.py
cp -v -u /media/Kindle/SotongDJ/record.sh ~/github/launchpad-kindle/record.sh
cp -v -u /media/Kindle/SotongDJ/system.py ~/github/launchpad-kindle/system.py
cp -v -u /media/Kindle/SotongDJ/test.sh ~/github/launchpad-kindle/test.sh
cp -v -u /media/Kindle/SotongDJ/python.py ~/github/launchpad-kindle/python.py
cp -v -u /media/Kindle/SotongDJ/changelog.txt ~/github/launchpad-kindle/changelog
cp -v -u /media/Kindle/launchpad/SotongDJ.ini ~/github/launchpad-kindle/launchpad/SotongDJ.ini
cp -v -u /media/Kindle/launchpad/mplayer.ini ~/github/launchpad-kindle/launchpad/mplayer.ini
cp -v -u /media/Kindle/mplayer/control.sh ~/github/launchpad-kindle/mplayer/control.sh
echo --------------------------------------------
echo remove temp files
rm -f /media/Kindle/SotongDJ/*temp
echo ============================================
