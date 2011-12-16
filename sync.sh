#!/bin/sh
echo ============================================
echo copy scripts
echo --------------------------------------------
cp -u /media/Kindle/SotongDJ/createlist.py ~/github/launchpad-kindle/createlist.py
cp -u /media/Kindle/SotongDJ/createlist.sh ~/github/launchpad-kindle/createlist.sh
cp -u /media/Kindle/SotongDJ/finance.sh ~/github/launchpad-kindle/finance.sh
cp -u /media/Kindle/SotongDJ/finance.py ~/github/launchpad-kindle/finance.py
cp -u /media/Kindle/SotongDJ/filter.py ~/github/launchpad-kindle/filter.py
cp -u /media/Kindle/SotongDJ/file.sh ~/github/launchpad-kindle/file.sh
cp -u /media/Kindle/SotongDJ/fm.py ~/github/launchpad-kindle/fm.py
cp -u /media/Kindle/SotongDJ/record.sh ~/github/launchpad-kindle/record.sh
cp -u /media/Kindle/SotongDJ/system.py ~/github/launchpad-kindle/system.py
cp -u /media/Kindle/SotongDJ/test.sh ~/github/launchpad-kindle/test.sh
cp -u /media/Kindle/SotongDJ/python.py ~/github/launchpad-kindle/python.py
cp -u /media/Kindle/SotongDJ/cmd.py ~/github/launchpad-kindle/cmd.py
cp -u /media/Kindle/SotongDJ/changelog.txt ~/github/launchpad-kindle/changelog
cp -u /media/Kindle/launchpad/SotongDJ.ini ~/github/launchpad-kindle/launchpad/SotongDJ.ini
cp -u /media/Kindle/launchpad/mplayer.ini ~/github/launchpad-kindle/launchpad/mplayer.ini
cp -u /media/Kindle/mplayer/control.sh ~/github/launchpad-kindle/mplayer/control.sh
cp -u /media/Kindle/SotongDJ/bozohttpd ~/github/launchpad-kindle/bozohttpd/bozohttpd
cp -u /media/Kindle/http/* ~/github/launchpad-kindle/gw4m4k/
## cp -u /media/Kindle/documents/KindleNote.azw2 ~/github/launchpad-kindle/kindlenote/KindleNote.azw2
## cp -u /media/Kindle/SotongDJ/developer.keystore ~/github/launchpad-kindle/kindlenote/developer.keystore
## cp -u /media/Kindle/SotongDJ/developer.keystore.txt ~/github/launchpad-kindle/kindlenote/developer.keystore.txt
echo --------------------------------------------
echo remove temp files
rm -f /media/Kindle/SotongDJ/*temp
echo ============================================
echo  Add change
git add -A
echo --------------------------------------------
echo Commit change
echo --------------------------------------------
echo Please enter your description of
echo this commit:
read commit
echo --------------------------------------------
git commit -m "$commit"
echo ============================================
echo Push commit\(s\) to GitHub
python ./gitcho.py nonch push origin
echo ============================================
