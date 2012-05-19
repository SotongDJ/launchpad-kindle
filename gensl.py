#!/mnt/us/python/bin/python2.6
import sys
import os
import config
## -----------Change it if different---------
global notepaddir,nonselectstate,nss,temp,playlist
notepaddir=config.general().get('notepaddir')
nonselectstate=config.general().get('nonselectstate')
nss=config.general().get('nss')
temp=config.general().get('temp')
playlist=config.general().get('playlist')
## ---------------words-------------------------------
global word01,selword01,word02,word03
word01=config.words('').get('word01')
selword01=config.words('').get('selword01')
#word02=config.words(thing).get('word02') #Please use 'Find' to find the command
word03=config.words('').get('word03')
## ---------------source folder-------------------------------
global musicdir,recorddir,strlist
musicdir=config.source().get('musicdir')
recorddir=config.source().get('recorddir')
strlist=config.source().get('strlist')
## ---------------list file head-------------------------------
global forpledit,forrecdit,forstrdit
forpledit=config.head().get('forpledit')
forrecdit=config.head().get('forrecdit')
forstrdit=config.head().get('forstrdit')
## ---------------temporary method-------------------------------
global letterset,purels
letterset=[['0','1','2','3','4','5','6','7','8','9'],['A','a'],['B','b'],['C','c'],['D','d'],['E','e'],['F','f'],['G','g'],['H','h'],['I','i'],['J','j'],['K','k'],['L','l'],['M','m'],['N','n'],['O','o'],['P','p'],['Q','q'],['R','r'],['S','s'],['T','t'],['U','u'],['V','v'],['W','w'],['X','x'],['Y','y'],['Z']]
purels=[]
for letters in letterset:
        for letter in letters:
            purels.append(letter)
## ----------------------------------------------
## Define function
## ----------------------------------------------
def mode(listh,enm):
    modef=open(listh+"-Mode.txt","w")
## Note:don't forget to change the case in control.sh
    if enm == 1:
        modef.write(word01+selword01)
        modef.close()
    elif enm == 0:
        modef.write(word01)
        modef.close()
## ----------------------------------------------
def gensl(otypes,source,listh,thing):
    status=os.system("ls -1 "+source+" > "+temp)
    types=otypes.split(".")
    songs=[]
    ## ---------------------Initial Library-------------------------
    library={}
    for letters in letterset[0:len(letterset)]:
        if letters[0] == '0':
            library.update({'Numbers':[]})
        else:
            library.update({letters[0]:[]})
    library.update({'Other':[]})
    ## ---------------------Filter Songs-------------------------
    for line in open(temp).read().splitlines():
        for type in types:
            if '#' not in line:
                if type in line:
                    songs.append(line)
    ## ---------------------Arrange Songs-------------------------
    for song in songs:
        for letters in letterset[0:len(letterset)]:
            for letter in letters:
                if letters[0] == '0':
                    if song[0] == letter:
                        library.get('Numbers').append(song)
                elif song[0] == letter:
                    library.get(letters[0]).append(song)
        if song[0] not in purels:
            library.get('Other').append(song)
    ## ---------------Calculate and Create Filelists---------------------
    filelib={}
    splitnum=50
    ## Start create selection of media which file name start with Numbers
    pagenum=1
    linenum=len(library.get("Numbers"))
    listf=open(listh+'-Part'+str(pagenum)+"-Num.txt",'w')
    listf.write(config.words(thing).get('word02'))
    listf.write(nonselectstate+nss.join(library.get("Numbers"))+'\n')
    ## Start create selection of media which file name start with alphabet
    for letters in letterset[1:len(letterset)-1]:
        tempnum=len(library.get(letters[0]))
        if library.get(letters[0])==[]:
            continue
        elif linenum+tempnum<splitnum:
            linenum=linenum+tempnum
            listf.write(nonselectstate+nss.join(library.get(letters[0]))+'\n')
        elif linenum+tempnum>=splitnum:
            if tempnum<=splitnum:
                pagenum=pagenum+1
                linenum=tempnum
                listf.close()
                listf=open(listh+'-Part'+str(pagenum)+"-"+letters[0]+".txt",'w')
                listf.write(config.words(thing).get('word02'))
                listf.write(nonselectstate+nss.join(library.get(letters[0]))+'\n')
            elif tempnum>splitnum:  ## Start seperate list when the number of items more then splitnum
                templistnum=0
                for ra in range(0,10000):
                    if templistnum+splitnum<=tempnum:
                        pagenum=pagenum+1
                        listf.close()
                        listf=open(listh+'-Part'+str(pagenum)+"-"+letters[0]+library.get(letters[0])[templistnum][1]+".txt",'w')
                        listf.write(config.words(thing).get('word02'))
                        listf.write(nonselectstate+nss.join(library.get(letters[0])[templistnum:(templistnum+splitnum+1)])+'\n')
                        templistnum=templistnum+splitnum
                    elif templistnum+splitnum>tempnum:
                        pagenum=pagenum+1
                        listf.close()
                        listf=open(listh+'-Part'+str(pagenum)+"-"+letters[0]+library.get(letters[0])[templistnum][1]+".txt",'w')
                        listf.write(config.words(thing).get('word02'))
                        listf.write(nonselectstate+nss.join(library.get(letters[0])[templistnum:(tempnum+1)])+'\n')
                        linenum=tempnum-templistnum
                        break
    ## Start create selection of media which file name start with non-latin characters
    tempnum=len(library.get("Other"))
    if linenum+tempnum<splitnum:
        linenum=linenum+tempnum
        listf.write(nonselectstate+nss.join(library.get("Other"))+'\n')
        listf.close()
    elif linenum+tempnum>=splitnum:
        if tempnum<=splitnum:
            pagenum=pagenum+1
            listf.close()
            listf=open(listh+'-Part'+str(pagenum)+"-Oth"+".txt",'w')
            listf.write(config.words(thing).get('word02'))
            listf.write(nonselectstate+nss.join(library.get("Other"))+'\n')
            listf.close()
        elif tempnum>splitnum:  ## Start seperate list when the number of items more then splitnum
            templistnum=0
            for ra in range(1,10001):
                if templistnum+splitnum<=tempnum:
                    pagenum=pagenum+1
                    listf.close()
                    listf=open(listh+'-Part'+str(pagenum)+"-Oth"+".txt",'w')
                    listf.write(config.words(thing).get('word02'))
                    listf.write(nonselectstate+nss.join(library.get("Other")[templistnum:(templistnum+splitnum+1)])+'\n')
                    templistnum=templistnum+splitnum
                elif templistnum+splitnum>tempnum:
                    pagenum=pagenum+1
                    listf.close()
                    listf=open(listh+'-Part'+str(pagenum)+"-Oth"+".txt",'w')
                    listf.write(config.words(thing).get('word02'))
                    listf.write(nonselectstate+nss.join(library.get("Other")[templistnum:(tempnum+1)])+'\n')
                    listf.close()
                    break
    status=os.system("rm "+temp)
## ----------------------------------------------
def gen4p():
    otypes="aac.flac.ogg.m4a.mp3.wav.wma"
    source=musicdir
    list=[]
    types=otypes.split(".")
    status=os.system("ls -1 "+source+" > "+temp)
    for line in open(temp).read().splitlines():
        for type in types:
            if  '.'+type in line:
                list.append(line)
    status=os.system("rm "+temp)
    return list
## ----------------------------------------------
def genm3u(source,listh):
    status=os.system("ls -1 "+source+" > "+temp)
    m3us=[]
    for line in open(temp).read().splitlines():
        if not '#' in line:
            if '.m3u' in line:
                m3us.append(line)
    if m3us  != []:
        m3uf=open(listh+"-Part0-m3u.txt",'w')
        m3uf.write(word03)
        m3uf.write(nonselectstate+nss.join(m3us)+'\n')
        m3uf.close()
    status=os.system("rm "+temp)
## ----------------------------------------------
def genstr(otypes,source,listh,thing):
    strs=[]
    for line in open(source).read().splitlines():
        if not '#' in line:
            if otypes in line:
                strs.append(line)
    strsf=open(listh+".txt",'w')
    strsf.write(config.words(thing).get('word02'))
    strsf.write(nonselectstate+nss.join(strs)+'\n')
    strsf.close()
## ----------------------------------------------
def clean(listh):
    status=os.system("rm "+listh+"*")
## ----------------------------------------------
## Order
## ----------------------------------------------
if "--playlist" in sys.argv:
    otypes="aac.flac.ogg.m4a.mp3.wav.wma"
    source=musicdir
    listh=forpledit
    thing='songs'
    clean(listh)
    gensl(otypes,source,listh,thing)
    mode(listh,1)
    genm3u(source,listh)
elif "--reclist" in sys.argv:
    otypes="wav"
    source=recorddir
    listh=forrecdit
    thing='records'
    clean(listh)
    gensl(otypes,source,listh,thing)
    mode(listh,0)
elif "--strlist" in sys.argv:
    otypes="http"
    source=strlist
    listh=forstrdit
    thing='stream/radio'
    clean(listh)
    genstr(otypes,source,listh,thing)
elif '--help' in sys.argv:
    print "gensl.py: Selection List Generator"
    print "Usage: "
    print "	python gensl.py { --playall | --playlist | --reclist | --strlist | --help }"
