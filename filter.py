#!/mnt/us/python/bin/python2.6
import sys
## -----------Change it if different---------
tempdir="/mnt/us/SotongDJ"
## ----------------------------------------------
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
if sys.argv[1] == "reclist":
    folder=tempdir+'/rectemp'
    thing='records'
if sys.argv[1] == "strlist":
    folder=tempdir+'/strtemp'
    thing='stream/radio'
types=sys.argv[2].split(".")
print "## Select the mode below by remove \'!\'"
print "## :!shuffle: :!playall:"
print "## Remove the \'!:\' to select your "+thing 
for type in types:
    for line in open(folder).read().splitlines():
        if not '##' in line:
            if  type in line:
                print '!:'+line

