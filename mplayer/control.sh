#!/bin/sh
## This version is edit by SotongDJ, base on mobileread one.
## See http://www.mobileread.com/forums/showthread.php?t=119851 for original control.sh

## /mnt/us is the root directory when mounting the Kindle via USB
INSTALLDIR=/mnt/us/mplayer
MUSICDIR=/mnt/us/music

pythonbin=/mnt/us/python/bin/python2.6
createlist=/mnt/us/SotongDJ/createlist.py

## Value between -20 and 19, decrease in case of music lags
NICENESS="-10"

FIFO=/tmp/mplayer.fifo
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

loadplaylist() {
    if ! cmd "loadlist $1"; then
		$MPLAYER -loop 0 -playlist $1 &
    fi
}


case "$1" in
    playall)
		$pythonbin $createlist playall > /tmp/mplayer.playlist
		loadplaylist /tmp/mplayer.playlist		
		;;
    playrand)
		$pythonbin $createlist playrand > /tmp/mplayer.playlist
		loadplaylist /tmp/mplayer.playlist
		;;
	playlist)
		$pythonbin $createlist playlist > /tmp/mplayer.playlist
		loadplaylist /tmp/mplayer.playlist
		;;
	playrec)
		$pythonbin $createlist reclist > /tmp/mplayer.playlist
		loadplaylist /tmp/mplayer.playlist
		;;
	playstr)
		$pythonbin $createlist strlist > /tmp/mplayer.playlist
		loadplaylist /tmp/mplayer.playlist
		;;
	fixyou)
		echo /mnt/us/music/FixYou.wav > /tmp/mplayer.playlist
		loadplaylist /tmp/mplayer.playlist
		;;
    pause)
		cmd "pause"
		;;
    stop)
	    killall mplayer
		;;
    prev)
		cmd "pt_step -1"
		;;
    next)
		cmd "pt_step 1"
		;;
    *)
		echo "Usage: $0 {playall|playrec|playrand|playlist|pause|stop|prev|next}"
		exit 1
		;;
esac

exit 0
