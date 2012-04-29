#!/mnt/us/python/bin/python2.6
import sys
import os
## -----------Change it if different---------
global temp,library,letterset
notepaddir="/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user"
temp="/tmp/filelisttemp"
## ---------------source folder-------------------------------
musicdir="/mnt/us/music"
recorddir="/mnt/us/record"
#strpldir="/mnt/us/music/playlist"
## ---------------list file head-------------------------------
forpledit=notepaddir+"/01-Playlist"
forrecdit=notepaddir+"/02-Reclist"
forstrdit=notepaddir+"/03-Strlist"
#forsdpldit=notepaddir+"/04-Playlists.txt"
## ---------------temporary method-------------------------------
letterset=[['0','1','2','3','4','5','6','7','8','9'],['A','a'],['B','b'],['C','c'],['D','d'],['E','e'],['F','f'],['G','g'],['H','h'],['I','i'],['J','j'],['K','k'],['L','l'],['M','m'],['N','n'],['O','o'],['P','p'],['Q','q'],['R','r'],['S','s'],['T','t'],['U','u'],['V','v'],['W','w'],['X','x'],['Y','y'],['Z'],'Other']
## ----------------------------------------------
## Define function
## ----------------------------------------------
def mode(listh):
    modef=open(listh+"-Mode.txt","w")
    modef.write("Select the mode below by remove \'!\', vice versa\n")
    modef.write("(mode is enabled by default)\n")
    modef.write(":!shuffle:\n")
## Note:don't forget to change the case in control.sh
    modef.write(":repeat:\n")
    modef.write(":!playall:")
    modef.close()
## ----------------------------------------------
def gensl(otypes,source,listh,thing):
    status=os.system("ls -1 "+source+" > "+temp)
    types=otypes.split(".")
    songs=[]
    ## ----------------------------------------------
    library={}
    for letters in letterset[0:len(letterset)]:
        if letters[0] == '0':
            library.update({'Numbers':[]})
        elif letters == 'Other':
            library.update({letters:[]})
        else:
            library.update({letters[0]:[]})
    ## ----------------------------------------------
    for line in open(temp).read().splitlines():
        for type in types:
            if not '#' in line:
                if type in line:
                    songs.append(line)
#d                    print line
    for song in songs:
#d        print 'song:'+song
        for letters in letterset[0:len(letterset)-1]:
#d            print 'letters:'+",".join(letters)
            for letter in letters:
#d                print 'letter:'+letter
                if letters[0] == '0':
                    if song[0] == letter:
#d                        print 'Numbers'+' '+letter+' '+song
                        library.get('Numbers').append(song)
                else:
                    if song[0] == letter:
#d                        print letters[0]+' '+letter+' '+song
                        library.get(letters[0]).append(song)
    num=len(library.get("Numbers"))
    print "Numbers"+'('+str(len(library.get("Numbers")))+')'+":" #d
    print "\n".join(library.get("Numbers"))+"\nSubtotal:"+str(num)+"\n" #d
#d    print library.get("Numbers")
    for letters in letterset[1:len(letterset)-1]:
        num=num+len(library.get(letters[0]))
        print letters[0]+'('+str(len(library.get(letters[0])))+')'+":" #d
        print "\n".join(library.get(letters[0]))+"\nSubtotal:"+str(num)+"\n" #d
    num=len(library.get("Other"))
    print "Other"+'('+str(len(library.get("Other")))+')'+":" #d
    print "\n".join(library.get("Other"))+"\nSubtotal:"+str(num)+"\n" #d
#d        print library.get(letters[0])
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
#    if "playlists" in sys.argv[-1]:
#        delay the development of this function
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
