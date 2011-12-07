import sys
import os
selbch=sys.argv[1]
status=os.system("git branch>/tmp/brchtemp")
for bch in open("/tmp/brchtemp").read().splitlines():
    if "*" in bch:
        bch=bch.replace(" ","")
        bch=bch.replace("*","")
        rmnbch=bch
if not rmnbch==selbch:
    cmd="git checkout "+selbch
    print "->"+cmd
    status=os.system(cmd)
