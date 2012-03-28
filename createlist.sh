#!/bin/sh
## -----------Change it if different---------
pythonbin=/mnt/us/python/bin/python
strpl=/mnt/us/mplayer/playlist
tempdir=/mnt/us/SotongDJ
notepaddir="/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user"
filterpy=/mnt/us/SotongDJ/filter.py
splitpy=/mnt/us/SotongDJ/split.py
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
listtemp="$tempdir/listtemp"

case "$1" in
    play)
        ls -1 $music > $playtemp
        $pythonbin $filterpy play aac.flac.ogg.m3u.m4a.mp3.wav.wma.m3p > "/tmp/playlist"
        ;;
    playlist)
        ls -1 $music > $playtemp
        $pythonbin $filterpy playlist aac.flac.ogg.m3u.m4a.mp3.wav.wma.m3p > $listtemp
        $pythonbin $splitpy playlist on
        rm $listtemp
        ;;
    playlists)
        ls -1 $notepaddir > $sdpltemp
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
