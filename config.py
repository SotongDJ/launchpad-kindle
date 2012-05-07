#!/mnt/us/python/bin/python2.6
import sys
## -----------General---------
def general():
    notepaddir="/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user"
    nonselectstate="!:"
    nss='\n'+nonselectstate
    temp="/tmp/filelisttemp"
    playlist="/tmp/mplayer.playlist"
    return {'notepaddir':notepaddir,'nonselectstate':nonselectstate,'nss':nss,'temp':temp,'playlist':playlist}
## ---------------words-------------------------------
def words(thing):
    nonselectstate=general().get('nonselectstate')
    word01="## Select the mode below by remove \'!\', vice versa\n## (mode is enabled by default)\n## :!playall: :!shuffle:"# :repeat:"
    selword01="\n##\n## m3u Control Section:\n## :!m3u: (Enable m3u)\n##(If you enable Shuffle and m3u at same time,\n##	the songs in m3u will be arrange ramdomly)"
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
    ordplayall=':playall:'
    ordshuffle=':shuffle:'
    ordm3u=':m3u:'
    return {'ordplayall':ordplayall,'ordshuffle':ordshuffle,'ordm3u':ordm3u}
## ------------Debug Usage-----------------------------
if '--test' in sys.argv:
    print general()
    print words('nothing')
    print source()
    print head()
    print oder()
elif '--help' in sys.argv:
    print "config.py: Strings Configuration"
    print "Usage: python config.py {--test|--help}"
