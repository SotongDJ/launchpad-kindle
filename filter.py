#!/mnt/us/python/bin/python2.6
import sys
## -----------Change it if different---------
tempdir="/mnt/us/SotongDJ"
## ----------------------------------------------
if sys.argv[1] == "playlist":
    folder=tempdir+'/playtemp'
    thing='songs'
    type='m4a'
if sys.argv[1] == "reclist":
    folder=tempdir+'/rectemp'
    thing='records'
    type='wav'
if sys.argv[1] == "strlist":
    folder=tempdir+'/strtemp'
    thing='stream/radio'
    type='http'
print "## Select the mode below by remove \'!\'"
print "## :!shuffle: :!playall:"
print "## Remove the \'!:\' to select your "+thing
for line in open(folder).read().splitlines():
    if not '##' in line:
        if  type in line:
            print '!:'+line

