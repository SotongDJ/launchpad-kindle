#!/mnt/us/python/bin/python2.6
import sys
import random
file = "/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user/02-Reclist.txt"
print file
print open(file).read().splitlines()
modenum=0
for line in open(file).read().splitlines():
    if "##" in line:
        if ":playall:" in line:
            modenum=modenum+1
            print modenum
        if ":shuffle:" in line:
            modenum=modenum+2
            print modenum
    if not '##' in line:
        if modenum == 0:
            print modenum
            if not '!:' in line:
                print '/mnt/us/music/'+line
        if modenum == 1:
            print modenum
            line=line.replace("!:","")
            print '/mnt/us/music/'+line
if modenum >= 2:
    lines=open(file).read().splitlines()
    print lines
    random.shuffle(lines)
    for line in lines:
        if not '##' in line:
            if modenum == 2:
                print modenum
                if not '!:' in line:
                    print '/mnt/us/music/'+line
            if modenum == 3:
                print modenum
                line=line.replace("!:","")
                print '/mnt/us/music/'+line
