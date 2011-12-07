import sys
import os
selbch=sys.argv[1]
status=os.system("git branch>./brchtemp")
for bch in open("./brchtemp").read().splitlines():
    if "*" in bch:
        bch=bch.replace(" ","")
        bch=bch.replace("*","")
        rmnbch=bch
if not rmnbch==selbch:
    cmd="git checkout "+selbch
    print "->"+cmd
    status=os.system(cmd)
