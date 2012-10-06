#!/bin/sh
## This version is edit by SotongDJ, base on mobileread one.
## See http://www.mobileread.com/forums/showthread.php?t=119851 for original control.sh

## /mnt/us is the root directory when mounting the Kindle via USB
INSTALLDIR=/mnt/us/mplayer
DOCLOGDIR=/mnt/us/documents/log
pythonbin=/mnt/us/python/bin/python2.6
genpl=/mnt/us/SotongDJ/genpl.py
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
				$MPLAYER $2 0 -playlist $1 &
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
		$pythonbin $genpl --playall
		$pythonbin $screensaver --action=turnoff --locker=lock
		loadplaylist /tmp/mplayer.playlist
		;;
	playrand)
		$pythonbin $genpl --playrand
		$pythonbin $screensaver --action=turnoff --locker=lock
		loadplaylist /tmp/mplayer.playlist
		;;
	playlist)
		$pythonbin $genpl --playlist
		$pythonbin $screensaver --action=turnoff --locker=lock
		loadplaylist /tmp/mplayer.playlist
		;;
	playrec)
		$pythonbin $genpl --reclist
		$pythonbin $screensaver --action=turnoff --locker=lock
		loadplaylist /tmp/mplayer.playlist
		;;
	playstr)
		$pythonbin $genpl --strlist
		$pythonbin $screensaver --action=turnoff --locker=lock
		loadplaylist /tmp/mplayer.playlist
		;;
	recent)
		$pythonbin $screensaver --action=turnoff --locker=lock
		loadplaylist /tmp/mplayer.playlist
		;;
	pause)
		cmd "pause"
		;;
	stop)
		killall mplayer
		$pythonbin $screensaver --action=turnon --locker=unlock
		;;
	prev)
		cmd "pt_step -1"
		;;
	next)
		cmd "pt_step 1"
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
