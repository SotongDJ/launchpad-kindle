#!/mnt/us/python/bin/python2.6
#coding=UTF8
## This py script was made to make sure the whole script set are using unique variable
import sys
import os
## =======================================================================
## -----------Change it if different---------
global configfile,npdir,kndir,logdir
configfile='/mnt/us/SotongDJ/SotongDJ.conf'
npdir='/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user'
kndir='/mnt/us/developer/KindleNote/work'
logdir='/mnt/us/documents/log'
## =======================================================================
## ---------------Argument---------------------------------
def argv(value,type):
    b=''
    for a in sys.argv:
        if type == 'boolean':
            if a == '--'+value:
                return 'true'
        if type == 'dtm':
            if value in a:
                return 'true'
        if type == 'acrdtm':
            if a == value:
                return 'true'
        if type == 'selection':
            if '--'+value+'=' in a:
                b=a.replace('--'+value+'=','')
                return b
## -----------value---------
#### -----------check value---------
def chkvlue(file):
    status=os.system('touch '+file)
    if open(file).read().splitlines() == []:
        return 'false'
    elif open(file).read().splitlines() != []:
        return 'true'
#### -----------read value---------
def rdvalue(file):
    lib={}
    for line in open(file).read().splitlines():
        if open(file).read().splitlines() != []:
            if len(line.split("=")) == 2:
                lib.update({line.split("=")[0]:line.split("=")[1]})
    return lib
#### -----------edit value---------
def edvalue(key,value,lib,path):
    lib.update({key:value})
    file=open(path,'w')
    for yek in lib:
        file.write(yek+'='+lib.get(yek)+'\n')
    file.close()
## -----------Determine---------
def viewvalue(key,defaultvalue,confpath):
    ## old name:determine()
    if chkvlue(confpath) == 'true':
        if rdvalue(confpath).get(key):
            return rdvalue(confpath).get(key)
        else:
            edvalue(key,defaultvalue,rdvalue(confpath),confpath)
            return defaultvalue
    elif chkvlue(confpath) == 'false':
        edvalue(key,defaultvalue,rdvalue(confpath),confpath)
        return defaultvalue
## ---------------Change---------------------------------
def change(value):
    thing=''
    status=os.system('rm '+npdir+'/00-ListLocateAt-*')
    status=os.system('rm '+kndir+'/00-ListLocateAt-*')
    edvalue('env',value,rdvalue(configfile),configfile)
    if value == 'notepad':
        thing='Notepad'
    elif value == 'kindlenote':
        thing='KindleNote'
    elif value == 'chinese':
        thing='KindleNote'
    status=os.system('touch '+npdir+'/00-ListLocateAt-'+thing+'.txt')
    status=os.system('touch '+kndir+'/00-ListLocateAt-'+thing+'.txt')
## =======================================================================
temp="/tmp/filelisttemp"
playlist="/tmp/mplayer.playlist"
def mpenv(): ##notepaddir,nonselectstate,nss,splitnum
    ## old name:general()
    select=viewvalue('env','kindlenote',configfile)
    ## -----------Kindle Editor Option---------
    ## What is your default editor in kindle?
    ## Answer:
    ## `notepad` for Notepad (7 Dragons)
    ## `kindlenote` for KindleNote (proDOOMman)
    ## `chinese` for KindleNote (proDOOMman) and the Kindle has PinYin IME
    if select == 'notepad':
        notepaddir=npdir
        splitnum=50
    else:
        notepaddir=kndir
        splitnum=20
    if select == 'chinese':
        nonselectstate='【不要】'
    else:
        nonselectstate="!:"
    nss='\n'+nonselectstate
    return {'notepaddir':notepaddir,'nonselectstate':nonselectstate,'nss':nss,'splitnum':splitnum}
## ---------------words-------------------------------
def words(thing):
    nonselectstate=mpenv().get('nonselectstate')
    select=viewvalue('env','kindlenote',configfile)
    if select == 'chinese':
        word01="## 去掉选项前的“不要”即可开启之，反之亦然。\n## 【不要全部播放】 【不要随机播放】\n##（注：重复模式默认开启，目前仍不能选择关闭。）"
        selword01="\n##\n## m3u 控制选项：\n## 【不要m3u】\n## （需不需要支持m3u播放列表播放。）\n## 注：\n##   当您同时选择开启m3u和随机播放时，\n##	  m3u列表里的所有歌曲会和其他歌曲一起乱序播放。\n"##\n## 【不要pl2m3u:NAME】\n## （需不需要把您要播放的媒体编成m3u播放列表,\n##  以NAME.m3u为名，如未更改NAME，将自动以时间日期命名）\n"
        word02="## 移除“"+nonselectstate+"”以选择您要播放的媒体（如歌曲及录音）。\n"
        word03="## 移除“"+nonselectstate+"”以选择您要播放的播放列表。\n"
    else:
        word01="## Select the mode below by remove \'!\', vice versa\n## (repeat mode is enabled by default)\n## :!playall: :!shuffle:"# :repeat:"
        selword01="\n##\n## m3u Control Section:\n## :!m3u: (m3u Playlist support)\n## (If you enable Shuffle and m3u at same time,\n##	 the songs in m3u will be arrange ramdomly)\n##\n"## :!pl2m3u:NAME: \n## (turn your choice(s) into a m3u playlist\n##  which name is \"NAME.m3u\", if \"NAME\" remain,\n## the name will be \"yymmddhhmm.m3u\")"
        word02="##Select the"+thing+"(s) you want to play by remove \'"+nonselectstate+"\'\n"
        word03="##Select the m3u playlist(s) you want to play by remove \'"+nonselectstate+"\'\n"
    return {'word01':word01,'selword01':selword01,'word02':word02,'word03':word03}
## ---------------source folder-------------------------------
musicdir="/mnt/us/music"
recorddir="/mnt/us/record"
strlist="/mnt/us/mplayer/playlist"
## ---------------list file head-------------------------------
forpledit=mpenv().get('notepaddir')+"/01-Playlist"
forrecdit=mpenv().get('notepaddir')+"/02-Reclist"
forstrdit=mpenv().get('notepaddir')+"/03-Strlist"
## ---------------Order---------------------------------
def oder():
    select=viewvalue('env','kindlenote',configfile)
    if select == 'chinese':
        ordplayall="【全部播放】"
        ordshuffle="【随机播放】"
        ordm3u="【m3u】"
        ordpl2m3u="【pl2m3u】"
    else:
        ordplayall=':playall:'
        ordshuffle=':shuffle:'
        ordm3u=':m3u:'
        ordpl2m3u=':pl2m3u:'
    return {'ordplayall':ordplayall,'ordshuffle':ordshuffle,'ordm3u':ordm3u,'ordpl2m3u':ordpl2m3u}
## =======================================================================
if argv('config.py','dtm') == 'true':
    if argv('key','selection') == 'test':
        print mpenv()
        print words('nothing')
        print source()
        print head()
        print oder()
    if argv('key','selection') == 'dtmtest':
        print viewvalue('env','kindlenote',configfile)
        print viewvalue('nowplaying','no',configfile)
    elif argv('key','selection') == 'change':
        print 'action=change'
        change(argv('value','selection'))
    elif '--help' in sys.argv:
        print "config.py: Strings Configuration"
        print "Usage: python config.py { --key=[KEY] --value=[VALUE]|--help }"
        print "\nKEY:\n        `test` for Debug Usage\n         `change` for Change Language and Editor which MyMplayer rely"
        print "\nVALUE:\n        `notepad` for Notepad (7 Dragons)\n         `kindlenote` for KindleNote (proDOOMman)\n         `chinese` for KindleNote (proDOOMman) and the Kindle has PinYin IME rely"
