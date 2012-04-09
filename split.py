#!/mnt/us/python/bin/python2.6
import sys
## -----------Change it if different---------
notepaddir="/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user/"
log="/mnt/us/SotongDJ/splittemp"
splitnum=50
## ----------------------------------------------
if sys.argv[-2] == "playlist":
    oripl="/mnt/us/SotongDJ/listtemp"
    filename="01-Playlist-Part"
if sys.argv[-2] == "nowplaying":
    oripl=notepaddir+"NowPlaying.txt"
    filename="NowPlaying-Page"
if sys.argv[-2] == "splite.py":
    oripl=notepaddir+"01-Playlist.txt"
    filename="01-Playlist-Part"
if sys.argv[-2] == "/mnt/us/SotongDJ/splite.py":
    oripl=notepaddir+"01-Playlist.txt"
    filename="01-Playlist-Part"

## ----------------------------------------------
if sys.argv[-1] == "on":
    file=open(oripl).read().splitlines()
    linenum=len(file)
#    print "linenum:"+str(linenum) ##debug usage
    pagenum=linenum/splitnum+1
#    print "pagenum:"+str(pagenum) ##debug usage
    lne=linenum+splitnum
    lns=linenum
    logf=open(log,"w")
    logf.write(str(pagenum))
    logf.close()
    for num1 in range(1,pagenum+1):
        lne=lne-splitnum
        lns=lns-splitnum
        splitpl=open(notepaddir+filename+str(pagenum+1-num1)+".txt","w")
        for num2 in range(lns+1,lne+1):
#            print str(num2) ##debug usage
            if num2 >= 1:
                splitpl.write(file[num2-1]+"\n")
    splitpl.close()
if sys.argv[-1] == "off":
    file=open(oripl,'w')
    pagenum=open(log).read()
    splitpl=[]
    for num1 in range(1,int(pagenum)+1):
        splitpl=splitpl+open(notepaddir+filename+str(num1)+".txt").read().splitlines()
    for line in splitpl:
        file.write(line+"\n")
    file.close()
if sys.argv[-1] == "split.py":
    print "Tips: python splite.py {playlist|nowplaying} {on|off}"
