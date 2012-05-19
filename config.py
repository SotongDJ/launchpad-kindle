#!/mnt/us/python/bin/python2.6
#coding=UTF8
import sys
import os
global config,select
## -----------Determine---------
def determine():
    ## -----------Kindle Editor Option---------
    ## What is your default editor in kindle?
    ## Answer:
    ## `notepad` for Notepad (7 Dragons)
    ## `kindlenote` for KindleNote (proDOOMman)
    ## `chinese` for KindleNote (proDOOMman) and the Kindle has PinYin IME
    default='chinese'
    temp='/tmp/edittemp'
    status=os.system('cat /mnt/us/SotongDJ/editor.conf>'+temp)
    if status == 0:
        for selection in ['notepad','kindlenote','chinese']:
            if selection in open(temp).read().splitlines():
                select=selection
    else:
        status=os.system('echo '+default+'>/mnt/us/SotongDJ/editor.conf')
        select=default
    return select
## -----------General---------
def general():
    select=determine()
    if select == 'notepad':
        notepaddir="/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user"
    else:
        notepaddir="/mnt/us/developer/KindleNote/work"
    if select == 'chinese':
        nonselectstate='【不要】'
    else:
        nonselectstate="!:"
    nss='\n'+nonselectstate
    temp="/tmp/filelisttemp"
    playlist="/tmp/mplayer.playlist"
    return {'notepaddir':notepaddir,'nonselectstate':nonselectstate,'nss':nss,'temp':temp,'playlist':playlist}
## ---------------words-------------------------------
def words(thing):
    nonselectstate=general().get('nonselectstate')
    select=determine()
    if select == 'chinese':
        word01="## 去掉选项前的“不要”即可开启之，反之亦然。\n## 【不要全部播放】 【不要随机播放】\n##（注：重复模式默认开启，目前仍不能选择关闭。）"
        selword01="\n##\n## m3u 控制选项：\n## 【不要m3u】\n## （需不需要支持m3u播放列表播放。）\n## 注：\n##   当您同时选择开启m3u和随机播放时，\n##	  m3u列表里的所有歌曲会和其他歌曲一起乱序播放。\n## 【不要pl2m3u:NAME】\n## （需不需要把您要播放的媒体编成m3u播放列表,\n##  以NAME.m3u为名，如未更改NAME，将自动以时间日期命名）"
        word02="## 移除“"+nonselectstate+"”以选择您要播放的媒体（如歌曲及录音）。"
        word03="## 移除“"+nonselectstate+"”以选择您要播放的播放列表。"
    else:
        word01="## Select the mode below by remove \'!\', vice versa\n## (repeat mode is enabled by default)\n## :!playall: :!shuffle:"# :repeat:"
        selword01="\n##\n## m3u Control Section:\n## :!m3u: (m3u Playlist support)\n## (If you enable Shuffle and m3u at same time,\n##	 the songs in m3u will be arrange ramdomly)\n## :!pl2m3u:NAME: \n## (turn your choice(s) into a m3u playlist\n##  which name is \"NAME.m3u\", if \"NAME\" remain,\n## the name will be \"yymmddhhmm.m3u\")"
        word02="##Select the"+thing+"(s) you want to play by remove \'"+nonselectstate+"\'\n"
        word03="##Select the m3u playlist(s) you want to play by remove \'"+nonselectstate+"\'\n"
    return {'word01':word01,'selword01':selword01,'word02':word02,'word03':word03}
## ---------------source folder-------------------------------
def source():
    musicdir="/mnt/us/music"
    recorddir="/mnt/us/record"
    strlist="/mnt/us/mplayer/playlist"
    return {'musicdir':musicdir,'recorddir':recorddir,'strlist':strlist}
## ---------------list file head-------------------------------
def head():
    notepaddir=general().get('notepaddir')
    forpledit=notepaddir+"/01-Playlist"
    forrecdit=notepaddir+"/02-Reclist"
    forstrdit=notepaddir+"/03-Strlist"
    return {'forpledit':forpledit,'forrecdit':forrecdit,'forstrdit':forstrdit}
## ---------------Order---------------------------------
def oder():
    select=determine()
    if select == 'chinese':
        ordplayall="【全部播放】"
        ordshuffle="【随机播放】"
        ordm3u="【m3u】"
    else:
        ordplayall=':playall:'
        ordshuffle=':shuffle:'
        ordm3u=':m3u:'
    return {'ordplayall':ordplayall,'ordshuffle':ordshuffle,'ordm3u':ordm3u}
## ---------------Argument---------------------------------
def argv(type):
    b=''
    for a in sys.argv:
        if '--'+type+'=' in a:
            b=a.replace('--'+type+'=','')
    return b
## ---------------Change---------------------------------
def change(value):
    thing=''
    status=os.system('rm /mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user/00-ListLocateAt-*')
    status=os.system('rm /mnt/us/developer/KindleNote/work/00-ListLocateAt-*')
    if value == 'notepad':
        thing='Notepad'
    elif value == 'kindlenote':
        thing='KindleNote'
    elif value == 'chinese':
        thing='KindleNote'
    status=os.system('echo '+value+'>/mnt/us/SotongDJ/editor.conf')
    status=os.system('touch /mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user/00-ListLocateAt-'+thing+'.txt')
    status=os.system('touch /mnt/us/developer/KindleNote/work/00-ListLocateAt-'+thing+'.txt')
    
## ------------Debug Usage-----------------------------
if argv('key') == 'test':
    print general()
    print words('nothing')
    print source()
    print head()
    print oder()
elif argv('key') == 'test':
    change(argv('value'))
elif '--help' in sys.argv:
    print "config.py: Strings Configuration"
    print "Usage: python config.py { --key=[KEY] --value=[VALUE]|--help }"
    print "\nKEY:\n        `test` for Debug Usage\n         `change` for Change Language and Editor which MyMplayer rely"
    print "\nVALUE:\n        `notepad` for Notepad (7 Dragons)\n         `kindlenote` for KindleNote (proDOOMman)\n         `chinese` for KindleNote (proDOOMman) and the Kindle has PinYin IME rely"
