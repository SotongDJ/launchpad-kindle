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
    pagenum=1
    linenum=len(library.get("Numbers"))
    listf=open(listh+'-Part'+str(pagenum)+"-Num.txt",'w')
    listf.write(config.words(thing).get('word02'))
    listf.write(nonselectstate+nss.join(library.get("Numbers"))+'\n')
    for letters in letterset[1:len(letterset)-1]:
        tempnum=len(library.get(letters[0]))
        if linenum+tempnum<splitnum:
            linenum=linenum+tempnum
            listf.write(nonselectstate+nss.join(library.get(letters[0]))+'\n')
        elif linenum+tempnum>=splitnum:
            pagenum=pagenum+1
            linenum=tempnum
            listf.close()
            listf=open(listh+'-Part'+str(pagenum)+"-"+letters[0]+".txt",'w')
            listf.write(config.words(thing).get('word02'))
            listf.write(nonselectstate+nss.join(library.get(letters[0]))+'\n')
    if linenum+len(library.get("Other"))<splitnum:
        linenum=linenum+tempnum
        listf.write(nonselectstate+nss.join(library.get("Other"))+'\n')
        listf.close()
    elif linenum+tempnum>=splitnum:
        pagenum=pagenum+1
        linenum=tempnum
        listf.close()
        listf=open(listh+'-Part'+str(pagenum)+"-Oth"+".txt",'w')
        listf.write(config.words(thing).get('word02'))
        listf.write(nonselectstate+nss.join(library.get("Other"))+'\n')
        listf.close()
## ----------------------------------------------
def gen4p(otypes,source):
    list=open("/tmp/playlist","w")
    types=otypes.split(".")
    status=os.system("ls -1 "+source+" > "+temp)
    for line in open(temp).read().splitlines():
        for type in types:
            if  '.'+type in line:
                list.write(line+"\n")
    list.close()
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
## Order
## ----------------------------------------------
if "--playall" in sys.argv:
    otypes="aac.flac.ogg.m4a.mp3.wav.wma"
    source=musicdir
    gen4p(otypes,source)
elif "--playlist" in sys.argv:
    otypes="aac.flac.ogg.m4a.mp3.wav.wma"
    source=musicdir
    listh=forpledit
    thing='songs'
    gensl(otypes,source,listh,thing)
    mode(listh,1)
    genm3u(source,listh)
elif "--reclist" in sys.argv:
    otypes="wav"
    source=recorddir
    listh=forrecdit
    thing='records'
    gensl(otypes,source,listh,thing)
    mode(listh,0)
elif "--strlist" in sys.argv:
    otypes="http"
    source=strlist
    listh=forstrdit
    thing='stream/radio'
    genstr(otypes,source,listh,thing)
else:
    print "gensl.py: Selection List Generator"
    print "Usage: "
    print "	python gensl.py { --playall | --playlist | --reclist | --strlist }"
