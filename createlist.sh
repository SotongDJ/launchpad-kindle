#!/bin/sh
## -----------Change it if different---------
rectemp=/mnt/us/SotongDJ/rectemp
playtemp=/mnt/us/SotongDJ/playtemp
strtemp=/mnt/us/SotongDJ/strtemp
pythonbin=/mnt/us/python/bin/python2.6
strpl=/mnt/us/mplayer/playlist
forpledit=/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user/01-Playlist.txt
forrecdit=/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user/02-Reclist.txt
forstrdit=/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user/03-Strlist.txt
filterpy=/mnt/us/SotongDJ/filter.py
music=/mnt/us/music
record=/mnt/us/record
## ----------------------------------------------

case "$1" in
	playlist)
		ls -1 $music > $playtemp
		$pythonbin $filterpy playlist > $forpledit
		;;
	reclist)
		ls -1 $record > $rectemp
		$pythonbin $filterpy reclist > $forrecdit
		;;
	strlist)
		cat $strpl > $strtemp
		$pythonbin $filterpy strlist > $forstrdit
		;;
	*)
		echo "Usage: $0 {playlist|reclist}"
		exit 1
		;;
esac

exit 0
