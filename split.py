#!/mnt/us/python/bin/python2.6
import sys
## -----------Change it if different---------
notepaddir="/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user/"
log="/mnt/us/SotongDJ/splitlog"
## ----------------------------------------------
oripl=notepaddir+"01-Playlist.txt"
if sys.argv[-1] == "on":
    file=open(oripl).read().splitlines()
    linenum=len(file)
    pagenum=linenum/90+1
    lne=linenum+90
    lns=linenum
    logf=open(log,"w")
    logf.write(str(pagenum))
    logf.close()
    for num1 in range(1,pagenum+1):
        lne=lne-90
        lns=lns-90
        splitpl=open(notepaddir+"01-Playlist-Part"+str(pagenum+1-num1)+".txt","w")
        for num2 in range(lns+1,lne+1):
            if num2 >= 1:
                splitpl.write(str(num2)+"\n")
    splitpl.close()
if sys.argv[-1] == "off":
    file=open(oripl,'w')
    pagenum=open(log).read()
    splitpl=[]
    for num1 in range(1,int(pagenum)+1):
        splitpl=splitpl+open(notepaddir+"01-Playlist-Part"+str(num1)+".txt").read().splitlines()
    for line in splitpl:
        file.write(line+"\n")
    file.close()
