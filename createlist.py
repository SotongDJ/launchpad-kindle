#!/mnt/us/python/bin/python2.6
import os
import sys
import random
## -----------Change it if different---------
notepaddir="/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user/"
musicdir="/mnt/us/music/"
recorddir="/mnt/us/record/"
## -------Temporary as dev gensl--------------
pythonbin="/mnt/us/python/bin/python2.6"
gensl="/mnt/us/SotongDJ/gensl.py"
## ----------------------------------------------
if sys.argv[1] == "playlist":
    #file = notepaddir+"01-Playlist.txt"
    file = "/mnt/us/SotongDJ/listtemp"
    targetdir=musicdir

if sys.argv[1] == "playall":
#    status=os.system("sh /mnt/us/SotongDJ/createlist.sh playall")
    status=os.system(pythonbin+" "+gensl+" --playall")
    file = "/tmp/playlist"
    targetdir=musicdir
if sys.argv[1] == "playrand":
    status=os.system(pythonbin+" "+gensl+" --playall")
    file = "/tmp/playlist"
    targetdir=musicdir

if sys.argv[1] == "reclist":
    file = notepaddir+"02-Reclist.txt"
    targetdir=recorddir
if sys.argv[1] == "strlist":
    file = notepaddir+"03-Strlist.txt"
    targetdir=""

if sys.argv[1] == "playlists":
    file = notepaddir+"04-Playlists.txt"
    sdpl=[]
##Playback Mode Description:
##modenum:
##   0 none
##   1 playall
##   2 shuffle
##   3 playall and shuffle
modenum=0
for line in open(file).read().splitlines():
    if sys.argv[1] == "playall":
        modenum=1
    if sys.argv[1] == "playrand":
        modenum=3
    if "##" in line:
        if ":playall:" in line:
            modenum=modenum+1
        if ":shuffle:" in line:
            modenum=modenum+2
    if not '##' in line:
        if modenum == 0:
            if not '!:' in line:
                if not sys.argv[1] == "playlists":
                    print targetdir+line
                if sys.argv[1] == "playlists":
                    sdpl.append(line)
        if modenum == 1:
            line=line.replace("!:","")
            if not sys.argv[1] == "playlists":
                print targetdir+line
            if sys.argv[1] == "playlists":
                sdpl.append(line)
##start another "if" as need to shuffle the file list in the begin
if modenum >= 2:
    lines=open(file).read().splitlines()
    random.shuffle(lines)
    for line in lines:
        if not '##' in line:
            if modenum == 2:
                if not '!:' in line:
                    if not sys.argv[1] == "playlists":
                        print targetdir+line
                    if sys.argv[1] == "playlists":
                        sdpl.append(line)
            if modenum == 3:
                line=line.replace("!:","")
                if not sys.argv[1] == "playlists":
                    print targetdir+line
                if sys.argv[1] == "playlists":
                    sdpl.append(line)
if sys.argv[1] == "playlists":
    final=[]
    for line in sdpl:
        final=final+open(notepaddir+line).read().splitlines()
    if modenum >= 2:
	    random.shuffle(final)
    for line in final:
        print line
