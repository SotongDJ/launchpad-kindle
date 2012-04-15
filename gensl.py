#!/mnt/us/python/bin/python2.6
import sys
import os
## -----------Change it if different---------
pythonbin="/mnt/us/python/bin/python"
notepaddir="/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user"
tempdir="/mnt/us/SotongDJ"
## ---------------source folder-------------------------------
musicdir="/mnt/us/music"
recorddir="/mnt/us/record"
#strpldir="/mnt/us/mplayer/playlist"
## ---------------temp folder-------------------------------
rectemp=tempdir+"/rectemp"
playtemp=tempdir+"/playtemp"
strtemp=tempdir+"/strtemp"
listtemp=tempdir+"/listtemp"
#sdpltemp=tempdir+"/sdpltemp"
## ---------------list file head-------------------------------
forpledit=notepaddir+"/01-Playlist"
forrecdit=notepaddir+"/02-Reclist"
forstrdit=notepaddir+"/03-Strlist"
#forsdpldit=notepaddir+"/04-Playlists.txt"
## ----------------------------------------------
## ----------------------------------------------
## Define function
## ----------------------------------------------
def mode(listh):
    modef=open(listh+"-Mode.txt","w")
    modef.write("Select the mode below by remove \'!\', vice versa\n")
    modef.write("(mode is enabled by default)\n")
    modef.write(":!shuffle:\n")
    modef.write(":repeat:\n")
## Note:don't forget to change the case in control.sh
    modef.write(":!playall:")
    modef.close()
## ----------------------------------------------
def gensl(otypes,source,temp,listh,thing):
    status=os.system("ls -1 "+source+" > "+temp)
    types=otypes.split(".")
#    for line in open(folder).read().splitlines():
    for type in types:
        for line in open(temp).read().splitlines():
            
    
    
    
    
    
    
    
## ----------------------------------------------
def gen4p(otypes,source,temp,listf):
    listt=open(listf,"w")
    types=otypes.split(".")
    status=os.system("ls -1 "+source+" > "+temp)
    for type in types:
        for line in open(temp).read().splitlines():
            if  type in line:
                listt.write(line+"\n")
    listt.close()
## ----------------------------------------------
## Order
## ----------------------------------------------
if "--" in sys.argv[-1]:
    if "playall" in sys.argv[-1]:
        otypes="aac.flac.ogg.m3u.m4a.mp3.wav.wma"
        source=musicdir
        temp=playtemp
        listf="/tmp/playlist"
        gen4p(otypes,source,temp,listf)
    if "playlist" in sys.argv[-1]:
        otypes="aac.flac.ogg.m3u.m4a.mp3.wav.wma"
        source=musicdir
        temp=playtemp
        listh=forpledit
        thing='songs'
        gensl(otypes,source,temp,thing)
#    if "playlists" in sys.argv[-1]:
#        delay the development of this function
    if "reclist" in sys.argv[-1]:
        otypes="wav"
        source=recorddir
        temp=rectemp
        listh=forrecdit
        thing='records'
        gensl(otypes,source,temp,thing)
    if "strlist" in sys.argv[-1]:
        otypes="http"
        source=strpldir
        temp=strtemp
        listh=forstrdit
        thing='stream/radio'
        gensl(otypes,source,temp,thing)
