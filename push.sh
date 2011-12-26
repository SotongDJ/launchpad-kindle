#!/bin/sh
echo ============================================
echo "copy scripts (copy file from com. to kindle)"
echo --------------------------------------------
cp -u ~/github/launchpad-kindle/createlist.py /media/Kindle/SotongDJ/createlist.py
cp -u ~/github/launchpad-kindle/createlist.sh /media/Kindle/SotongDJ/createlist.sh
cp -u ~/github/launchpad-kindle/finance.sh /media/Kindle/SotongDJ/finance.sh
cp -u ~/github/launchpad-kindle/finance.py /media/Kindle/SotongDJ/finance.py
cp -u ~/github/launchpad-kindle/filter.py /media/Kindle/SotongDJ/filter.py
cp -u ~/github/launchpad-kindle/file.sh /media/Kindle/SotongDJ/file.sh
cp -u ~/github/launchpad-kindle/fm.py /media/Kindle/SotongDJ/fm.py
cp -u ~/github/launchpad-kindle/record.sh /media/Kindle/SotongDJ/record.sh
cp -u ~/github/launchpad-kindle/system.py /media/Kindle/SotongDJ/system.py
cp -u ~/github/launchpad-kindle/test.sh /media/Kindle/SotongDJ/test.sh
cp -u ~/github/launchpad-kindle/python.py /media/Kindle/SotongDJ/python.py
cp -u ~/github/launchpad-kindle/cmd.py /media/Kindle/SotongDJ/cmd.py
cp -u ~/github/launchpad-kindle/changelog /media/Kindle/SotongDJ/changelog.txt
cp -u ~/github/launchpad-kindle/launchpad/SotongDJ.ini /media/Kindle/launchpad/SotongDJ.ini
cp -u ~/github/launchpad-kindle/launchpad/mplayer.ini /media/Kindle/launchpad/mplayer.ini
cp -u ~/github/launchpad-kindle/mplayer/control.sh /media/Kindle/mplayer/control.sh
cp -u ~/github/launchpad-kindle/bozohttpd/bozohttpd /media/Kindle/SotongDJ/bozohttpd
cp -u ~/github/launchpad-kindle/gw4m4k/* /media/Kindle/http/
echo --------------------------------------------
echo remove temp files
rm -f /media/Kindle/SotongDJ/*temp
echo ============================================
