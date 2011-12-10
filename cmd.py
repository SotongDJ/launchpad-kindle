#!/mnt/us/python/bin/python2.6
import os
import sys
global cmdfile,notepaddir,cmdtemp
## -----------Change it if different---------
notepaddir="/mnt/us/developer/KindleNote/work/"
cmdfile=notepaddir+"CMD.TXT"
workdir="/mnt/us/SotongDJ/"
## ----------------------------------------------
result=notepaddir+"Result.txt"
cmdtemp=workdir+"cmdtemp"
def head():
    status=os.system("echo ---------------------------------------------------->>"+result)
    status=os.system("date +%Y-%m-%d.%H:%M:%S >>"+result)
    status=os.system("echo ---------------------------------------------------->>"+result)
def cmdfunc():
    file=open(cmdfile,'w')
    part='## Write down the command you prefer to run, \n## please make sure you replace \" with \\\".'
    file.write(part)
    file.close()
def rmcmdf():
    rmlist=[]
    status=os.system("ls -1 "+notepaddir+">"+workdir+"cmdtemp")
    for line in open(cmdtemp).read().splitlines():
        if 'cmd' in line:
            rmlist.append(notepaddir+"\""+line+"\"")
    for rm in rmlist:
        status=os.system("rm -f "+rm)
    status=os.system("rm -f "+workdir+"cmdtemp")
##
if len(sys.argv)==1:
    print "Usage: "+sys.argv[0]+" {file|list}"
elif sys.argv[1] == 'file':
    cmdsq=[]
    cmdlist=[]
    maindict={}
    maxnum=0
    status=os.system("ls -1 "+notepaddir+">"+workdir+"cmdtemp")
    for line in open(cmdtemp).read().splitlines():
        subdict={}
        if 'cmd' in line:
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
    for num in range(maxnum):
        num=num+1
        cmd=maindict[num]
        cmd="\""+cmd+"\""
        cmdlist.append(cmd)
    cmd='&&'.join(cmdlist)
    head()
    status=os.system(cmd+">>"+result)
    rmcmdf()
elif sys.argv[1] == 'list':
    cmdlist=[]
    for cmd in open(cmdfile).read().splitlines():
        if not "##" in cmd:
            cmd="\""+cmd+"\""
            cmdlist.append(cmd)
    cmd='&&'.join(cmdlist)
    head()
    status=os.system(cmd+">>"+result)
    cmdfunc()
elif sys.argv[1] == 'init':
    cmdfunc()
    rmcmdf()
