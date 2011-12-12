#!/bin/sh
## -----------Change it if different---------
pythonbin=/mnt/us/python/bin/python2.6
strpl=/mnt/us/mplayer/playlist
tempdir=/mnt/us/SotongDJ
notepaddir=/mnt/us/developer/KindleNote/work
filterpy=/mnt/us/SotongDJ/filter.py
music=/mnt/us/music
record=/mnt/us/record
## ----------------------------------------------
forpledit="$notepaddir/01-Playlist.txt"
forrecdit="$notepaddir/02-Reclist.txt"
forstrdit="$notepaddir/03-Strlist.txt"
forsdpldit="$notepaddir/04-Playlists.txt"
rectemp="$tempdir/rectemp"
playtemp="$tempdir/playtemp"
strtemp="$tempdir/strtemp"
sdpltemp="$tempdir/sdpltemp"

case "$1" in
    play)
        ls -1 $music > $playtemp
        $pythonbin $filterpy play aac.flac.ogg.m3u.m4a.mp3.wav.wma > "/tmp/playlist"
        ;;
    playlist)
        ls -1 $music > $playtemp
        ls -1 $notepaddir > $sdpltemp
        $pythonbin $filterpy playlist aac.flac.ogg.m3u.m4a.mp3.wav.wma > $forpledit
        $pythonbin $filterpy playlists sdpl > $forsdpldit
        ;;
    reclist)
        ls -1 $record > $rectemp
        $pythonbin $filterpy reclist wav> $forrecdit
        ;;
    strlist)
        cat $strpl > $strtemp
        $pythonbin $filterpy strlist http> $forstrdit
        ;;
    *)
        echo "Usage: $0 {playlist|reclist}"
        exit 1
        ;;
esac

exit 0
