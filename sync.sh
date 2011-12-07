#!/bin/sh
echo ============================================
echo copy scripts
echo --------------------------------------------
cp -u -v /media/Kindle/SotongDJ/createlist.py ~/github/launchpad-kindle/createlist.py
cp -u -v /media/Kindle/SotongDJ/createlist.sh ~/github/launchpad-kindle/createlist.sh
cp -u -v /media/Kindle/SotongDJ/finance.sh ~/github/launchpad-kindle/finance.sh
cp -u -v /media/Kindle/SotongDJ/finance.py ~/github/launchpad-kindle/finance.py
cp -u -v /media/Kindle/SotongDJ/filter.py ~/github/launchpad-kindle/filter.py
cp -u -v /media/Kindle/SotongDJ/file.sh ~/github/launchpad-kindle/file.sh
cp -u -v /media/Kindle/SotongDJ/fm.py ~/github/launchpad-kindle/fm.py
cp -u -v /media/Kindle/SotongDJ/record.sh ~/github/launchpad-kindle/record.sh
cp -u -v /media/Kindle/SotongDJ/system.py ~/github/launchpad-kindle/system.py
cp -u -v /media/Kindle/SotongDJ/test.sh ~/github/launchpad-kindle/test.sh
cp -u -v /media/Kindle/SotongDJ/python.py ~/github/launchpad-kindle/python.py
cp -u -v /media/Kindle/SotongDJ/changelog.txt ~/github/launchpad-kindle/changelog
cp -u -v /media/Kindle/launchpad/SotongDJ.ini ~/github/launchpad-kindle/launchpad/SotongDJ.ini
cp -u -v /media/Kindle/mplayer/control.sh ~/github/launchpad-kindle/mplayer/control.sh
## cp -u -v /media/Kindle/documents/KindleNote.azw2 ~/github/launchpad-kindle/kindlenote/KindleNote.azw2
## cp -u -v /media/Kindle/SotongDJ/developer.keystore ~/github/launchpad-kindle/kindlenote/developer.keystore
## cp -u -v /media/Kindle/SotongDJ/developer.keystore.txt ~/github/launchpad-kindle/kindlenote/developer.keystore.txt
echo --------------------------------------------
echo remove gedit backup files
rm -f /media/Kindle/SotongDJ/*~
rm -f /mnt/us/SotongDJ/*~
rm -f ~/github/launchpad-kindle/*~
rm -f ~/github/launchpad-kindle/*/*~
rm -f /media/Kindle/launchpad/*~
rm -f /mnt/us/launchpad/*~
rm -f /media/Kindle/mplayer/*~
rm -f /mnt/us/mplayer/*~
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
git push origin testing
echo ============================================
