#!/mnt/us/python/bin/python2.6
import os
import sys
## -----------Change it if different---------
notepaddir="/mnt/us/developer/KindleNote/work/"
workdir="/mnt/us/SotongDJ/"
## ----------------------------------------------
cmdtemp=workdir+"cmdtemp"
result=notepaddir+"Result.txt"
rmlist=[]
cmdsq=[]
maindict={}
maxnum=0
status=os.system("ls -1 "+notepaddir+">"+workdir+"cmdtemp")
for line in open(cmdtemp).read().splitlines():
    subdict={}
    if 'cmd' in line:
        rmlist.append(notepaddir+line)
        line=line.replace('.txt','')
        line=line.replace('cmd','')
        precmdsq=line.split("-")
        for sec in precmdsq:
            if not  sec=='':
                cmdsq.append(sec)
        nums=cmdsq[0]
        cmdsq.remove(nums)
        numi=int(nums)
        if numi>maxnum:
            maxnum=numi
        tcmd=' '.join(cmdsq)
        subdict={numi:tcmd}
        maindict=dict(maindict.items()+subdict.items())
status=os.system("echo ---------------------------------------------------->>"+result)
status=os.system("date +%Y-%m-%d.%H:%M:%S >>"+result)
status=os.system("echo ---------------------------------------------------->>"+result)
for num in range(maxnum):
    num=num+1
    cmd=maindict[num]
    status=os.system(cmd+">>"+result)
for rm in rmlist:
    status=os.system("rm -f "+rm)
