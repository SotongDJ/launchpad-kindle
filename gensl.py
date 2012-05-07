#!/mnt/us/python/bin/python2.6
import sys
import os
## -----------Change it if different---------
global notepaddir,nonselectstate,nss,temp,playlist,letterset,purels
notepaddir="/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user"
nonselectstate="!:"
nss='\n'+nonselectstate
temp="/tmp/filelisttemp"
## ---------------source folder-------------------------------
musicdir="/mnt/us/music"
recorddir="/mnt/us/record"
## ---------------list file head-------------------------------
forpledit=notepaddir+"/01-Playlist"
forrecdit=notepaddir+"/02-Reclist"
forstrdit=notepaddir+"/03-Strlist"
## ---------------temporary method-------------------------------
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
    word="## Select the mode below by remove \'!\', vice versa\n## (mode is enabled by default)\n## :!playall: :!shuffle:"# :repeat:"
    selword="\n##\n## m3u Control Section:\n## :!m3u: (Enable m3u)\n##(If you enable Shuffle and m3u at same time,\n##	the songs in m3u will be arrange ramdomly)"
## Note:don't forget to change the case in control.sh
    if enm == 1:
        modef.write(word+selword)
        modef.close()
    elif enm == 0:
        modef.write(word)
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
    word="##Select the"+thing+"(s) you want to play by remove \'"+nonselectstate+"\'\n"
    linenum=len(library.get("Numbers"))
    listf=open(listh+'-Part'+str(pagenum)+"-Num.txt",'w')
    listf.write(word)
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
            listf.write(word)
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
        listf.write(word)
        listf.write(nonselectstate+nss.join(library.get("Other"))+'\n')
        listf.close()
## ----------------------------------------------
def gen4p(otypes,source):
    list=open("/tmp/playlist","w")
    types=otypes.split(".")
    status=os.system("ls -1 "+source+" > "+temp)
    for type in types:
        for line in open(temp).read().splitlines():
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
        word="##Select the m3u playlist(s) you want to play by remove \'"+nonselectstate+"\'\n"
        m3uf=open(listh+"-Part0-m3u.txt",'w')
        m3uf.write(word)
        m3uf.write(nonselectstate+nss.join(m3us)+'\n')
        m3uf.close()
## ----------------------------------------------
def genstr(otypes,source,listh,thing):
    strs=[]
    for line in open(source).read().splitlines():
        if not '#' in line:
            if otypes in line:
                strs.append(line)
    word="##Select the "+thing+"(s) you want to play by remove \'"+nonselectstate+"\'\n"
    strsf=open(listh+".txt",'w')
    strsf.write(word)
    strsf.write(nonselectstate+nss.join(strs)+'\n')
    strsf.close()
## ----------------------------------------------
## Order
## ----------------------------------------------
if "--playall" in sys.argv:
    otypes="aac.flac.ogg.m3u.m4a.mp3.wav.wma"
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
    source="/mnt/us/mplayer/playlist"
    listh=forstrdit
    thing='stream/radio'
    genstr(otypes,source,listh,thing)
