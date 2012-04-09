#!/bin/sh
## This version is edit by SotongDJ, base on mobileread one.
## See http://www.mobileread.com/forums/showthread.php?t=119851 for original control.sh

## /mnt/us is the root directory when mounting the Kindle via USB
INSTALLDIR=/mnt/us/mplayer
MUSICDIR=/mnt/us/music
NOTEDIR=/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user
DOCLOGDIR=/mnt/us/documents/log
pythonbin=/mnt/us/python/bin/python
createlist=/mnt/us/SotongDJ/createlist.py
screensaver=/mnt/us/SotongDJ/screen.py

## Value between -20 and 19, decrease in case of music lags
NICENESS="-10"

FIFO=/tmp/mplayer.fifo
##MPLAYER="nice -n$NICENESS $INSTALLDIR/mplayer -ao alsa -slave -input file=$FIFO"
MPLAYER="nice -n$NICENESS $INSTALLDIR/mplayer -ao alsa -slave -quiet -input file=$FIFO"
SHUF="$INSTALLDIR/shuf"

if [ ! -e $FIFO ]; then
  mkfifo $FIFO
fi


cmd() {
	if [ "x$(pidof mplayer)" = "x" ]; then
		return 1;
	fi
	echo "$@" > $FIFO
	return 0;
}

case "$2" in
	noneloop)
		loadplaylist() {
			if ! cmd "loadlist $1"; then
				$MPLAYER 0 -playlist $1 &
			fi
		}
		;;
	*)
		loadplaylist() {
			if ! cmd "loadlist $1"; then
				$MPLAYER -loop 0 -playlist $1 &
			fi
		}
		;;
esac


case "$1" in
	playall)
		$pythonbin $createlist playall > /tmp/mplayer.playlist
		cp /tmp/mplayer.playlist $DOCLOGDIR/NowPlaying.txt
		loadplaylist /tmp/mplayer.playlist
		$pythonbin $screensaver turnoff
		;;
	playrand)
		$pythonbin $createlist playrand > /tmp/mplayer.playlist
		cp /tmp/mplayer.playlist $DOCLOGDIR/NowPlaying.txt
		loadplaylist /tmp/mplayer.playlist
		$pythonbin $screensaver turnoff
		;;
	playlist)
		$pythonbin /mnt/us/SotongDJ/split.py playlist off
		$pythonbin $createlist playlist > /tmp/mplayer.playlist
		rm /mnt/us/SotongDJ/listtemp
		cp /tmp/mplayer.playlist $DOCLOGDIR/NowPlaying.txt
		loadplaylist /tmp/mplayer.playlist
		$pythonbin $screensaver turnoff
		;;
	playlists)
		$pythonbin $createlist playlists > /tmp/mplayer.playlist
		loadplaylist /tmp/mplayer.playlist
		$pythonbin $screensaver turnoff
		;;
	playrec)
		$pythonbin $createlist reclist > /tmp/mplayer.playlist
		loadplaylist /tmp/mplayer.playlist
		$pythonbin $screensaver turnoff
		;;
	playstr)
		$pythonbin $createlist strlist > /tmp/mplayer.playlist
		loadplaylist /tmp/mplayer.playlist
		$pythonbin $screensaver turnoff
		;;
	prepl)
		cp /tmp/mplayer.playlist $DOCLOGDIR/NowPlaying.txt
		loadplaylist /tmp/mplayer.playlist
		$pythonbin $screensaver turnoff
		;;
	pause)
		cmd "pause"
		;;
	stop)
		killall mplayer
		$pythonbin $screensaver turnon
		;;
	prev)
		cmd "pt_step -1"
		;;
	next)
		cmd "pt_step 1"
		;;
	test)
#		echo>testtemp
		cmd "get_meta_title">testtemp
		cmd "get_meta_artist">testtemp
		cmd "get_percent_pos">testtemp
		cmd "get_time_pos">testtemp
		cmd "get_time_length">testtemp
#		cat testtemp
		;;
	volup)
		cmd "volume 5"
		;;
	voldown)
		cmd "volume -5"
		;;
	*)
		echo "Usage: $0 {playall|playrec|playrand|playlist|pause|stop|prev|next}"
		exit 1
		;;
esac

exit 0
