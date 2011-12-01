#!/mnt/us/python/bin/python2.6
import sys
import random
## -----------Change it if different---------
notepaddir="/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user/"
## ----------------------------------------------
if sys.argv[1] == "playlist":
    file = notepaddir+"01-Playlist.txt"
    targetdir="/mnt/us/music/"
if sys.argv[1] == "reclist":
    file = notepaddir+"02-Reclist.txt"
    targetdir="/mnt/us/record/"
if sys.argv[1] == "strlist":
    file = notepaddir+"03-Strlist.txt"
    targetdir=""
##Playback Mode Description:
##modenum:
##   0 none
##   1playall
##   2 shuffle
##   3 playall and shuffle
modenum=0
for line in open(file).read().splitlines():
    if "##" in line:
        if ":playall:" in line:
            modenum=modenum+1
        if ":shuffle:" in line:
            modenum=modenum+2
    if not '##' in line:
        if modenum == 0:
            if not '!:' in line:
                print targetdir+line
        if modenum == 1:
            line=line.replace("!:","")
            print targetdir+line
##start another "if" as need to shuffle the file list in the begin
if modenum >= 2:
    lines=open(file).read().splitlines()
    random.shuffle(lines)
    for line in lines:
        if not '##' in line:
            if modenum == 2:
                if not '!:' in line:
                    print targetdir+line
            if modenum == 3:
                line=line.replace("!:","")
                print targetdir+line
