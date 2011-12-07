#!/bin/sh
echo ============================================
echo copy scripts
cp /media/Kindle/SotongDJ/createlist.py ~/github/launchpad-kindle/createlist.py
cp /media/Kindle/SotongDJ/createlist.sh ~/github/launchpad-kindle/createlist.sh
cp /media/Kindle/SotongDJ/finance.sh ~/github/launchpad-kindle/finance.sh
cp /media/Kindle/SotongDJ/finance.py ~/github/launchpad-kindle/finance.py
cp /media/Kindle/SotongDJ/filter.py ~/github/launchpad-kindle/filter.py
cp /media/Kindle/SotongDJ/file.sh ~/github/launchpad-kindle/file.sh
cp /media/Kindle/SotongDJ/fm.py ~/github/launchpad-kindle/fm.py
cp /media/Kindle/SotongDJ/record.sh ~/github/launchpad-kindle/record.sh
cp /media/Kindle/SotongDJ/system.py ~/github/launchpad-kindle/system.py
cp /media/Kindle/SotongDJ/test.sh ~/github/launchpad-kindle/test.sh
cp /media/Kindle/SotongDJ/try.py ~/github/launchpad-kindle/try.py
cp /media/Kindle/SotongDJ/changelog.txt ~/github/launchpad-kindle/changelog
cp /media/Kindle/launchpad/SotongDJ.ini ~/github/launchpad-kindle/launchpad/SotongDJ.ini
cp /media/Kindle/mplayer/control.sh ~/github/launchpad-kindle/mplayer/control.sh
## cp /media/Kindle/documents/KindleNote.azw2 ~/github/launchpad-kindle/kindlenote/KindleNote.azw2
## cp /media/Kindle/SotongDJ/developer.keystore ~/github/launchpad-kindle/kindlenote/developer.keystore
## cp /media/Kindle/SotongDJ/developer.keystore.txt ~/github/launchpad-kindle/kindlenote/developer.keystore.txt
echo --------------------------------------------
echo remove gedit backup files
rm -f /media/Kindle/SotongDJ/*~
rm -f ~/github/launchpad-kindle/*~
rm -f /media/Kindle/launchpad/*~
rm -f /media/Kindle/mplayer/*~
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
git push origin master
echo ============================================
