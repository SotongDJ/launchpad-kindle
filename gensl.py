#!/mnt/us/python/bin/python2.6
import sys
import os
## -----------Change it if different---------
pythonbin="/mnt/us/python/bin/python"
strpl="/mnt/us/mplayer/playlist"
tempdir="/mnt/us/SotongDJ"
notepaddir="/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user"
music="/mnt/us/music"
record="/mnt/us/record"
## ----------------------------------------------
forpledit=notepaddir+"/01-Playlist.txt"
forrecdit=notepaddir+"/02-Reclist.txt"
forstrdit=notepaddir+"/03-Strlist.txt"
forsdpldit=notepaddir+"/04-Playlists.txt"
## ----------------------------------------------
rectemp=tempdir+"/rectemp"
playtemp=tempdir+"/playtemp"
strtemp=tempdir+"/strtemp"
sdpltemp=tempdir+"/sdpltemp"
listtemp=tempdir+"/listtemp"
## ----------------------------------------------
## Define function
## ----------------------------------------------
def arrange():
    
    
    
    
## ----------------------------------------------
## Order
## ----------------------------------------------
if "--" in sys.argv[-1]:
    if "play" in sys.argv[-1]:
        status=os.system("ls -1 "+music+" > "+playtemp)
    if "playlist" in sys.argv[-1]:
        status=os.system("ls -1 "+music+" > "+playtemp)
##    if "playlists" in sys.argv[-1]:
##        delay the development of this function
    if "reclist" in sys.argv[-1]:
        status=os.system("ls -1 "+record+" > "+rectemp)
    if "strlist" in sys.argv[-1]:
        status=os.system("ls -1 "+strpl+" > "+strtemp)

