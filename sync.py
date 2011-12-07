import sys
import os
selbch=sys.argv[1]
status=os.system("git branch>./brchtemp")
for bch in open("./brchtemp").read().splitlines():
    if "*" in bch:
        bch=bch.replace(" ","")
        bch=bch.replace("*","")
        rmnbch=bch
if rmnbch==selbch:
    cmd="git push origin "+selbch
    print "->"+cmd
    status=os.system(cmd)
if not rmnbch==selbch:
    cmd="git checkout "+selbch
    print "->"+cmd
    status=os.system(cmd)
    cmd="git push origin "+selbch
    print "->"+cmd
    status=os.system(cmd)
    cmd="git checkout "+rmnbch
    print "->"+cmd
    status=os.system(cmd)
