#!/bin/sh
echo ============================================
echo "copy scripts (copy file from com. to kindle)"
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
cp -v -u ~/github/launchpad-kindle/createlist.py /media/Kindle/SotongDJ/createlist.py
cp -v -u ~/github/launchpad-kindle/createlist.sh /media/Kindle/SotongDJ/createlist.sh
cp -v -u ~/github/launchpad-kindle/finance.sh /media/Kindle/SotongDJ/finance.sh
cp -v -u ~/github/launchpad-kindle/finance.py /media/Kindle/SotongDJ/finance.py
cp -v -u ~/github/launchpad-kindle/filter.py /media/Kindle/SotongDJ/filter.py
cp -v -u ~/github/launchpad-kindle/file.sh /media/Kindle/SotongDJ/file.sh
cp -v -u ~/github/launchpad-kindle/fm.py /media/Kindle/SotongDJ/fm.py
cp -v -u ~/github/launchpad-kindle/tree.py /media/Kindle/SotongDJ/tree.py
cp -v -u ~/github/launchpad-kindle/split.py /media/Kindle/SotongDJ/split.py
cp -v -u ~/github/launchpad-kindle/screen.py /media/Kindle/SotongDJ/screen.py
cp -v -u ~/github/launchpad-kindle/record.sh /media/Kindle/SotongDJ/record.sh
cp -v -u ~/github/launchpad-kindle/system.py /media/Kindle/SotongDJ/system.py
cp -v -u ~/github/launchpad-kindle/test.sh /media/Kindle/SotongDJ/test.sh
cp -v -u ~/github/launchpad-kindle/python.py /media/Kindle/SotongDJ/python.py
cp -v -u ~/github/launchpad-kindle/changelog /media/Kindle/SotongDJ/changelog.txt
cp -v -u ~/github/launchpad-kindle/launchpad/SotongDJ.ini /media/Kindle/launchpad/SotongDJ.ini
cp -v -u ~/github/launchpad-kindle/launchpad/mplayer.ini /media/Kindle/launchpad/mplayer.ini
cp -v -u ~/github/launchpad-kindle/mplayer/control.sh /media/Kindle/mplayer/control.sh
echo --------------------------------------------
echo remove temp files
rm -f /media/Kindle/SotongDJ/*temp
echo ============================================
