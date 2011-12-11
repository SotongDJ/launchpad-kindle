#!/mnt/us/python/bin/python2.6
import os
import sys
global cmdfile,notepaddir,cmdtemp,bcheck,acheck
## -----------Change it if different---------
notepaddir=open("protect").read().replace("\n","")+"/"
workdir="/mnt/us/SotongDJ/"
## ----------------------------------------------
cmdfile=notepaddir+"command.txt"
result=notepaddir+"Result.txt"
cmdtemp=workdir+"cmdtemp"
bcheck=[]
acheck=[]
def head():
    status=os.system("echo ---------------------------------------------------->>"+result)
    status=os.system("date +%Y-%m-%d.%H:%M:%S >>"+result)
    status=os.system("echo ---------------------------------------------------->>"+result)
def cmdfunc():
    filea=open(cmdfile,'w')
    parta='## Write down the command you prefer to run, \n## please make sure you replace \" with \\\".'
    filea.write(parta)
    filea.close()
def rmcmdf():
    rmlist=[]
    status=os.system("ls -1 "+notepaddir+">"+workdir+"cmdtemp")
    for line in open(cmdtemp).read().splitlines():
        if 'cmd' in line:
            rmlist.append(notepaddir+"\""+line+"\"")
    for rm in rmlist:
        status=os.system("rm -f "+rm)
    status=os.system("rm -f "+workdir+"cmdtemp")
    cmd2file=notepaddir+"TipsForCmdPyFile.txt"
    fileq=open(cmd2file,'w')
    partq='## You can replace = with !1, \n## You can replace $ with !2, \n## You can replace " with !3, \n## Don\'t modify this file'
    fileq.write(partq)
    fileq.close()
def chkfunc():
    for sect in bcheck:
        if "rm " in sect:
            sect=sect.replace('rm ','mv ')
            sect=sect+"/mnt/us/SotongDJ/trash/"
            acheck.append(sect)
        elif "mv " in sect:
            if "-b" in sect:
                sect=sect
                acheck.append(sect)
            elif "--backup" in sect:
                sect=sect
                acheck.append(sect)
            else:
                sect=sect.replace('mv ','mv -b ')
                acheck.append(sect)
        elif "cp " in sect:
            if "-b" in sect:
                sect=sect
                acheck.append(sect)
            elif "--backup" in sect:
                sect=sect
                acheck.append(sect)
            else:
                sect=sect.replace('cp ','cp -b ')
                acheck.append(sect)
        else:
            sect=sect
            acheck.append(sect)
##
##
if len(sys.argv)==1:
    print "Usage: "+sys.argv[0]+" {file|list}"
elif sys.argv[1] == 'files':
    cmdlist=[]
    maindict={}
    maxnum=0
    status=os.system("ls -1 "+notepaddir+">"+workdir+"cmdtemp")
    for line in open(cmdtemp).read().splitlines():
        subdict={}
        cmdsq=[]
        if 'cmd' in line:
            line=line.replace('.txt','')
            line=line.replace('cmd','')
            line=line.replace('!1','=')
            line=line.replace('!2','$')
            line=line.replace('!3','\"')
            precmdsq=line.split("-")
            for sec in precmdsq:
                if not  sec=='':
                    cmdsq.append(sec)
#                    print cmdsq
            nums=cmdsq[0]
#            print nums
            cmdsq.remove(nums)
            numi=int(nums)
            if numi>maxnum:
                maxnum=numi
            tcmd=' '.join(cmdsq)
            subdict={numi:tcmd}
#            print subdict
            maindict=dict(maindict.items()+subdict.items())
#            print maindict
    for num in range(maxnum):
        num=num+1
        cmd=maindict[num]
        cmdlist.append(cmd)
    bcheck=cmdlist
    chkfunc()
    cmdlist=acheck
    cmd='&&'.join(cmdlist)
    head()
#    print cmd+">>"+result
    status=os.system(cmd+">>"+result)
    rmcmdf()
    cmdfunc()
elif sys.argv[1] == 'list':
    cmdlist=[]
    for cmd in open(cmdfile).read().splitlines():
        if not "##" in cmd:
            cmdlist.append(cmd)
    bcheck=cmdlist
    chkfunc()
    cmdlist=acheck
    cmd='&&'.join(cmdlist)
    head()
#    print cmd+">>"+result
    status=os.system(cmd+">>"+result)
    cmdfunc()
elif sys.argv[1] == 'init':
    rmcmdf()
    cmdfunc()
