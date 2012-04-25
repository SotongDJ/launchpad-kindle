#!/mnt/us/python/bin/python2.6
import sys
import os
## -----------Change it if different---------
notepaddir="/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user"
temp="/tmp/filelisttemp"
## ---------------source folder-------------------------------
musicdir="/mnt/us/music"
recorddir="/mnt/us/record"
#strpldir="/mnt/us/music/playlist"
## ---------------list file head-------------------------------
forpledit=notepaddir+"/01-Playlist"
forrecdit=notepaddir+"/02-Reclist"
forstrdit=notepaddir+"/03-Strlist"
#forsdpldit=notepaddir+"/04-Playlists.txt"
## ----------------------------------------------
## Define function
## ----------------------------------------------
def mode(listf):
    modef=open(listf+"-Mode.txt","w")
    modef.write("Select the mode below by remove \'!\', vice versa\n")
    modef.write("(mode is enabled by default)\n")
    modef.write(":!shuffle:\n")
    modef.write(":repeat:\n")
## Note:don't forget to change the case in control.sh
    modef.write(":!playall:")
    modef.close()
## ----------------------------------------------
def gensl(otypes,source,listf,thing):
    status=os.system("ls -1 "+source+" > "+temp)
    types=otypes.split(".")
#    for type in types:
#        for line in open(temp).read().splitlines():
            
    
    
    
    
    
    
    
## ----------------------------------------------
def gen4p(otypes,source):
    list=open("/tmp/playlist","w")
    types=otypes.split(".")
    status=os.system("ls -1 "+source+" > "+temp)
    for type in types:
        for line in open(temp).read().splitlines():
            if  type in line:
                list.write(line+"\n")
    list.close()
## ----------------------------------------------
## Order
## ----------------------------------------------
if "--" in sys.argv[-1]:
    if "playall" in sys.argv[-1]:
        otypes="aac.flac.ogg.m3u.m4a.mp3.wav.wma"
        source=musicdir
        gen4p(otypes,source)
    if "playlist" in sys.argv[-1]:
        otypes="aac.flac.ogg.m3u.m4a.mp3.wav.wma"
        source=musicdir
        listf=forpledit
        thing='songs'
        gensl(otypes,source,thing)
#    if "playlists" in sys.argv[-1]:
#        delay the development of this function
    if "reclist" in sys.argv[-1]:
        otypes="wav"
        source=recorddir
        listf=forrecdit
        thing='records'
        gensl(otypes,source,thing)
    if "strlist" in sys.argv[-1]:
        otypes="http"
        source=strpldir
        listf=forstrdit
        thing='stream/radio'
        gensl(otypes,source,thing)
