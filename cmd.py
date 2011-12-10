#!/mnt/us/python/bin/python2.6
import os
import sys
global cmdfile
## -----------Change it if different---------
notepaddir="/mnt/us/developer/KindleNote/work/"
cmdfile=notepaddir+"CMD.TXT"
workdir="/mnt/us/SotongDJ/"
## ----------------------------------------------
result=notepaddir+"Result.txt"
def head():
    status=os.system("echo ---------------------------------------------------->>"+result)
    status=os.system("date +%Y-%m-%d.%H:%M:%S >>"+result)
    status=os.system("echo ---------------------------------------------------->>"+result)
def cmdfunc():
    file=open(cmdfile,'w')
    part='## Write down the command you prefer to run, \n## please make sure you replace \" with \\\".'
    file.write(part)
    file.close()
if len(sys.argv)==1:
    print "Usage: "+sys.argv[0]+" {file|list}"
elif sys.argv[1] == 'file':
    cmdtemp=workdir+"cmdtemp"
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
    head()
    for num in range(maxnum):
        num=num+1
        cmd=maindict[num]
    status=os.system(cmd+">>"+result)
    for rm in rmlist:
        status=os.system("rm -f "+rm)
elif sys.argv[1] == 'list':
    cmdlist=[]
    for cmd in open(cmdfile).read().splitlines():
        if not "##" in cmd:
            cmdlist.append(cmd)
    cmd='&&'.join(cmdlist)
    head()
    status=os.system(cmd+">>"+result)
    cmdfunc()
