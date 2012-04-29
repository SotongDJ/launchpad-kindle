#!/mnt/us/python/bin/python2.6
import sys
import os
import random
## -----------Change it if different---------
global notepaddir,nonselectstate,temp,playlist
notepaddir="/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user"
nonselectstate="!:"
temp="/tmp/filelisttemp"
playlist="/tmp/mplayer.playlist"
## ---------------source folder-------------------------------
musicdir="/mnt/us/music"
recorddir="/mnt/us/record"
## ---------------list file head-------------------------------
forpledit="01-Playlist"
forrecdit="02-Reclist"
forstrdit="03-Strlist"
## -------Temporary as dev gensl--------------
pythonbin="/mnt/us/python/bin/python2.6"
gensl="/mnt/us/SotongDJ/gensl.py"
## ----------------------------------------------
## Define function
##    #        #            #                #                    #
## ----------------------------------------------
def ouput(result):
    file=open(playlist,'w')
    for line in result:
        file.write(line+"\n")
    file.close()
## --------------for test--------------------------------
def ouputtest(result):
    print '\n'.join(result)
## ----------------------------------------------
def process(sets,modenum,source):
    result=[]
    for obj in sets:
        if modenum== 0:
            if nonselectstate not in obj:
                result.append(source+'/'+obj)
        elif modenum<10:
            if modenum in [1,3]:
                result.append(source+'/'+obj.replace(nonselectstate,''))
        elif modenum>=10:
            if modenum not in [11,13]:
                if nonselectstate not in obj:
                    if ".m3u" not in obj:
                        result.append(source+'/'+obj)
                    elif ".m3u" in obj:
                        for line in open(source+'/'+obj).read().splitlines():
                            result.append(line)
            elif modenum in [11,13]:
                if ".m3u" not in obj:
                    result.append(source+'/'+obj.replace(nonselectstate,''))
                elif ".m3u" in obj:
                    for line in open(source+'/'+obj.replace(nonselectstate,'')).read().splitlines():
                        result.append(line)
    if modenum<10:
        if modenum>=2:
            random.shuffle(result)
            random.shuffle(result)
            random.shuffle(result)
    elif modenum>=12:
        random.shuffle(result)
        random.shuffle(result)
        random.shuffle(result)
    return result
## ----------------------------------------------
def ascertain(listh):
    #Mode
    #None -0
    #Playall - 1
    #Shuffle -2
    #m3u - 10
    modenum=0
    modefile=notepaddir+'/'+listh+"-Mode.txt"
    for line in open(modefile).read().splitlines():
        if ':playall:' in line:
            modenum=modenum+1
        if ':shuffle:' in line:
            modenum=modenum+2
        if ':m3u:' in line:
            modenum=modenum+10
#    print str(modenum)
    return modenum
## ----------------------------------------------
def genlist(source,listh):
    status=os.system("ls -1 "+notepaddir+" > "+temp)
    sets=[]
    for files in open(temp).read().splitlines():
        if listh in files[0:len(listh)]:
            for line in open(notepaddir+'/'+files).read().splitlines():
                if '#' not in line:
                    sets.append(line)
    return sets
## ----------------------------------------------
def convlist(plist):
    sets=[]
    for line in open(plist).read().splitlines():
        if '#' not in line:
            if nonselectstate not in line:
                sets.append(line)
    return sets
## ----------------------------------------------
## Order
## ----------------------------------------------
if "--playall" in sys.argv:
    status=os.system(pythonbin+" "+gensl+" --playall")
    source=musicdir
    plist="/tmp/playlist"
    modenum=11
    ouput(process(convlist(plist),modenum,source))
elif "--playrand" in sys.argv:
    status=os.system(pythonbin+" "+gensl+" --playall")
    source=musicdir
    plist="/tmp/playlist"
    modenum=13
    ouput(process(convlist(plist),modenum,source))
elif "--playlist" in sys.argv:
    source=musicdir
    listh=forpledit
    ouput(process(genlist(source,listh),ascertain(listh),source))
elif "--reclist" in sys.argv:
    source=recorddir
    listh=forrecdit
    ouput(process(genlist(source,listh),ascertain(listh),source))
elif "--strlist" in sys.argv:
    listh=forstrdit
    plist=notepaddir+'/'+listh+".txt"
    ouput(process(convlist(plist),ascertain(listh),source))
## ----------------------------------------------
