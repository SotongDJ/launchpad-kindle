import sys
import os
## =========================================
global cmd,target
## =========================================
def argv(type):
    b=''
    for a in sys.argv:
        if '--'+type+'=' in a:
            b=a.replace('--'+type+'=','')
    return b
## -----------------------------------------
def num(number):
    if int(number) <10:
        return '00'+number
    elif int(number) >=10:
        if int(number) <100:
            return '0'+number
        elif int(number) >=999:
            print 'S.N.Error'
            exit()
        elif int(number) >=100:
            return number
## -----------------------------------------
def bch(mode):
    status=os.system("git branch>/tmp/brchtemp")
    if mode != '':
        for bch in open("/tmp/brchtemp").read().splitlines():
            if mode in bch:
                bch=bch.replace(" ","")
                bch=bch.replace("*","")
                return bch
    elif mode == '':
        bchl=[]
        for bch in open("/tmp/brchtemp").read().splitlines():
            if mode in bch:
                bch=bch.replace(" ","")
                bch=bch.replace("*","")
                bchl.append(bch)
        return ' '.join(bchl)
    status=os.system("rm /tmp/brchtemp")
## =========================================
if argv('mode') == 'ifnot':
    if not bch('*')==argv('target'):
        target=argv('target')
if argv('mode') == 'list':
    target=argv('target')+' '+bch('')
## -----------------------------------------
if argv('action') == 'checkout':
        cmd="git "+argv('action')+" "+target
if argv('action') == 'push':
        cmd="git "+argv('action')+" "+target
if argv('action') == 'commit':
        cmd="git "+argv('action')+" -m \"["+argv('date')+num(argv('serial'))+"] "+argv('commit')+"\""
## -----------------------------------------
print "->"+cmd
status=os.system(cmd)
## -----------------------------------------
