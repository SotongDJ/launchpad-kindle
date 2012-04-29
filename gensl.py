#!/mnt/us/python/bin/python2.6
import sys
import os
## -----------Change it if different---------
global temp,library,letterset,purels,nonselectstate
notepaddir="/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user"
nonselectstate="!:"
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
def mode(listh):
    modef=open(listh+"-Mode.txt","w")
    word="## Select the mode below by remove \'!\', vice versa\n## (mode is enabled by default)\n## :!playall: :!shuffle: :repeat:\n##\n## m3u Control Section:\n## :!m3u: (Enable m3u) :!shufflesongs:\n##(Shuffle will just random the m3u playlist only, to ramdom the songs, enable Shufflem3u and the songs in m3u will be ramdom"
## Note:don't forget to change the case in control.sh
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
            if not '#' in line:
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
    word="##Select the song(s) you want to play by remove \'"+nonselectstate+"\'"
    linenum=len(library.get("Numbers"))
    print listh+"-from-Numbers.txt"
    print word
    print "\n".join(library.get("Numbers"))
    for letters in letterset[1:len(letterset)-1]:
        tempnum=len(library.get(letters[0]))
        if linenum+tempnum<splitnum:
            linenum=linenum+tempnum
            print "\n".join(library.get(letters[0]))
        elif linenum+tempnum>=splitnum:
            pagenum=pagenum+1
            linenum=tempnum
            print listh+"-from-"+letters[0]+".txt"
            print word
            print "\n".join(library.get(letters[0]))
    if linenum+len(library.get("Other"))<splitnum:
        linenum=linenum+tempnum
        print "\n".join(library.get("Other"))
    elif linenum+tempnum>=splitnum:
        pagenum=pagenum+1
        linenum=tempnum
        print listh+"-from-"+"Other"+".txt"
        print word
        print "\n".join(library.get("Other"))
    
    ## ---------------------Debug Usage-------------------------
#d    num=len(library.get("Numbers"))
#d    print "Numbers"+'('+str(len(library.get("Numbers")))+')'+":"
#d    print "\n".join(library.get("Numbers"))+"\nSubtotal:"+str(num)+"\n"
#d    for letters in letterset[1:len(letterset)]:
#d        num=num+len(library.get(letters[0]))
#d        print letters[0]+'('+str(len(library.get(letters[0])))+')'+":"
#d        print "\n".join(library.get(letters[0]))+"\nSubtotal:"+str(num)+"\n"
#d    num=len(library.get("Other"))
#d    print "Other"+'('+str(len(library.get("Other")))+')'+":"
#d    print "\n".join(library.get("Other"))+"\nSubtotal:"+str(num)+"\n"
## ----------------------------------------------
def gen4p(otypes,source):
    list=open("/tmp/playlist","w")
    types=otypes.split(".")
    status=os.system("ls -1 "+source+" > "+temp)
    for type in types:
        for line in open(temp).read().splitlines():
            if  type in line:
                list.write(line+"\n")
    list.close()
## ----------------------------------------------
## Order
## ----------------------------------------------
if "--playall" in sys.argv[-1]:
    otypes="aac.flac.ogg.m3u.m4a.mp3.wav.wma"
    source=musicdir
    gen4p(otypes,source)
if "--playlist" in sys.argv[-1]:
    otypes="aac.flac.ogg.m3u.m4a.mp3.wav.wma"
    source=musicdir
    listh=forpledit
    thing='songs'
    gensl(otypes,source,listh,thing)
if "--reclist" in sys.argv[-1]:
    otypes="wav"
    source=recorddir
    listh=forrecdit
    thing='records'
    gensl(otypes,source,listh,thing)
if "--strlist" in sys.argv[-1]:
    otypes="http"
    source=strpldir
    listh=forstrdit
    thing='stream/radio'
    gensl(otypes,source,listh,thing)
