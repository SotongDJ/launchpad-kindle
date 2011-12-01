#!/bin/sh
## See http://www.mplayerhq.hu/DOCS/tech/slave.txt for docs

## /mnt/us is the root directory when mounting the Kindle via USB
INSTALLDIR=/mnt/us/mplayer
MUSICDIR=/mnt/us/music
##RECDIR=/mnt/us/record
PLAYLIST="$INSTALLDIR/playlist"

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

listmusic() {
    ## We can't allow non-valid file in the playlist because it would make prev behave weirdly
    find $MUSICDIR -type f -regex '.*\.\(3gp\|aac\|flac\|ogg\|m3u\|m4a\|mp3\|pls\|wav\|wma\)'
}

## listrecord() {
 ##    find $RECDIR -type f -regex '.*\.\(3gp\|aac\|flac\|ogg\|m3u\|m4a\|mp3\|pls\|wav\|wma\)'
## }

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
        listmusic > /tmp/mplayer.playlist
        loadplaylist /tmp/mplayer.playlist
        ;;
##	playrec)
##        listrecord > /tmp/mplayer.playlist
##        loadplaylist /tmp/mplayer.playlist
##        ;;
    playrand)
        listmusic | $SHUF > /tmp/mplayer.playlist
        loadplaylist /tmp/mplayer.playlist
        ;;
#    playlist)
#        loadplaylist $PLAYLIST
#        ;;
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
