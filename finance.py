#!/mnt/us/python/bin/python2.6
import sys
## -----------Change it if different---------
finatemp="/mnt/us/SotongDJ/finatemp"
notepaddir="/mnt/us/.active-content-data/8a5982e82ae68fb2012bc688405e0026/work/user/"
## ----------------------------------------------
lastdatenum=0
for line in open(finatemp).read().splitlines():
    if "money-" in line:
        line=line.replace("money-","")
        line=line.replace(".txt","")
        if int(line) >  lastdatenum:
            lastdatenum=int(line)
if int(sys.argv[1]) == lastdatenum:
    exit()
file=open(notepaddir+"money-"+sys.argv[1]+".txt","w")
temple="n:none\n----------------\ncost:\nn\ntotal n\n----------------\nborrow:\nn\ntotal n\n----------------\nlent:\nn\ntotal n\n================\nmoney add:\nmain n\nleft-left n\nleft-right n\nright-left n\nright-right n\nlittle n\n----------------\nmoney left:\nmain n\nleft-left n\nleft-right n\nright-left n\nright-right n\nlittle n\n----------------\n"
file.write(temple)
file.close()
