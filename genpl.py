#!/mnt/us/python/bin/python2.6
import sys
import os
import random
import config
import gensl
## -----------Change it if different---------
global notepaddir,nonselectstate,nss,temp,playlist
notepaddir=config.mpenv().get('notepaddir')
nonselectstate=config.mpenv().get('nonselectstate')
nss=config.mpenv().get('nss')
temp=config.mpenv().get('temp')
playlist=config.mpenv().get('playlist')
## ---------------source folder-------------------------------
global musicdir,recorddir
musicdir=config.source().get('musicdir')
recorddir=config.source().get('recorddir')
## ---------------list file head-------------------------------
global forpledit,forrecdit,forstrdit
forpledit=config.head().get('forpledit')
forrecdit=config.head().get('forrecdit')
forstrdit=config.head().get('forstrdit')
## ---------------Order---------------------------------
global ordplayall,ordshuffle,ordm3u
ordplayall=config.oder().get('ordplayall')
ordshuffle=config.oder().get('ordshuffle')
ordm3u=config.oder().get('ordm3u')
## ----------------------------------------------
## Define function
##    #        #            #                #                    #
## ----------------------------------------------
def ouput(result,source):
    file=open(playlist,'w')
    for line in result:
        file.write(source+'/'+line+"\n")
    file.close()
    if config.viewvalue('nowplaying','no',config.configfile) == 'yes':
        file2=open(config.logdir+'/NowPlaying.txt','w')
        file2.write("\n".join(result))
        file2.close()
## --------------for test--------------------------------
def ouputtest(result):
    print '\n'.join(result)
## ----------------------------------------------
def process(sets,modenum):
    result=[]
    for obj in sets:
        if modenum== 0:
            if nonselectstate not in obj:
                result.append(obj)
        elif modenum<10:
            if modenum in [1,3]:
                result.append(obj.replace(nonselectstate,''))
        elif modenum>=10:
            if modenum not in [11,13]:
                if nonselectstate not in obj:
                    if ".m3u" not in obj:
                        result.append(obj)
                    elif ".m3u" in obj:
                        for line in open(obj).read().splitlines():
                            result.append(line)
            elif modenum in [11,13]:
                if ".m3u" not in obj:
                    result.append(obj.replace(nonselectstate,''))
                elif ".m3u" in obj:
                    for line in open(obj.replace(nonselectstate,'')).read().splitlines():
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
    modefile=listh+"-Mode.txt"
    for line in open(modefile).read().splitlines():
        if ordplayall in line:
            modenum=modenum+1
        if ordshuffle in line:
            modenum=modenum+2
        if ordm3u in line:
            modenum=modenum+10
#    print str(modenum)
    return modenum
## ----------------------------------------------
def genlist(source,listh):
    status=os.system("ls -1 "+notepaddir+" > "+temp)
    sets=[]
    for files in open(temp).read().splitlines():
        if listh.replace(notepaddir+'/','') in files:
            for line in open(notepaddir+'/'+files).read().splitlines():
                if '#' not in line:
                    sets.append(line)
    status=os.system("rm "+temp)
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
##if config.dtmargv('gensl.py') == 'true':
if "--playall" in sys.argv:
    ouput(process(gensl.gen4p(),11),musicdir)
elif "--playrand" in sys.argv:
    ouput(process(gensl.gen4p(),13),musicdir)
elif "--playlist" in sys.argv:
    source=musicdir
    listh=forpledit
    ouput(process(genlist(source,listh),ascertain(listh)),source)
elif "--reclist" in sys.argv:
    source=recorddir
    listh=forrecdit
    ouput(process(genlist(source,listh),ascertain(listh)),source)
elif "--strlist" in sys.argv:
    listh=forstrdit
    plist=notepaddir+'/'+listh+".txt"
    ouput(process(convlist(plist),ascertain(listh)),source)
elif '--help' in sys.argv:
    print "genpl.py: Playlist Generator"
    print "Usage: "
    print "	python genpl.py { --playall | --playrand | --playlist | --reclist | --strlist | --help }"
