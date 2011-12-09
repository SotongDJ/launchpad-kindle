import sys
import os
if sys.argv[1] == "change":
    selbch=sys.argv[3]
    status=os.system("git branch>/tmp/brchtemp")
    for bch in open("/tmp/brchtemp").read().splitlines():
        if "*" in bch:
            bch=bch.replace(" ","")
            bch=bch.replace("*","")
            rmnbch=bch
    if not rmnbch==selbch:
        cmd="git "+sys.argv[2]+" "+selbch
        print "->"+cmd
        status=os.system(cmd)
if sys.argv[1] == "nonch":
    status=os.system("git branch>/tmp/brchtemp")
    for bch in open("/tmp/brchtemp").read().splitlines():
        if "*" in bch:
            bch=bch.replace(" ","")
            bch=bch.replace("*","")
            rmnbch=bch
    cmd="git "+sys.argv[2]+" "+sys.argv[3]+" "+rmnbch
    print "->"+cmd
    status=os.system(cmd)
