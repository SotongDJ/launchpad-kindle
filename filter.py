#!/mnt/us/python/bin/python2.6
import sys
## -----------Change it if different---------
tempdir="/mnt/us/SotongDJ"
## ----------------------------------------------
global thing
thing=""
def showa():
    print "## Select the mode below by remove \'!\'"
    print "## :!shuffle: :!playall:"
    print "## Remove the \'!:\' to select your "+thing 
def showb():
    print "## Pls prepare your sdpl file before on computer"
    print "## The name of sdpl must follow the format below:"
    print "## myfavpl-sdpl.txt or MyFav-sDPl.TXt p.s.no capital sensitive"
    print "## The content format of sdpl you can refer from example-sdpl.txt"
    print "##------------------"
    print "## Select the mode below by remove \'!\'"
    print "## :!playall: select all the"+thing+"that you have"
    print "## :!shuffle: shuffle the"+thing+"that you select"
    print "##------------------"
    print "## Remove the \'!:\' to select your "+thing 
if len(sys.argv) == 1:
    print "Usage: "+sys.argv[0]+" {play|playlist|playlists|reclist|strlist}"
if sys.argv[1] == "play":
    folder=tempdir+'/playtemp'
    thing='songs'
    types=sys.argv[2].split(".")
    for type in types:
        for line in open(folder).read().splitlines():
            if not '##' in line:
                if  type in line:
                    print line
    exit()
if sys.argv[1] == "playlist":
    folder=tempdir+'/playtemp'
    thing='songs'
    showa()
if sys.argv[1] == "playlists":
    folder=tempdir+'/sdpltemp'
    thing='playlist(s)'
    showb()
if sys.argv[1] == "reclist":
    folder=tempdir+'/rectemp'
    thing='records'
    showa()
if sys.argv[1] == "strlist":
    folder=tempdir+'/strtemp'
    thing='stream/radio'
    showa()
types=sys.argv[2].split(".")
for line in open(folder).read().splitlines():
    if not '##' in line:
        for type in types:
            if  type in line:
                print '!:'+line
