#!/mnt/us/python/bin/python2.6
import os
import sys
os.system("touch /tmp/pslog")
offcmd="lipc-set-prop com.lab126.powerd preventScreenSaver 1"
oncmd="lipc-set-prop com.lab126.powerd preventScreenSaver 0"
pslog=open("/tmp/pslog").read().replace("\n","")
if "--action=turnoff" in sys.argv:
    if "off" not in pslog:
        os.system("echo off>/tmp/pslog")
        os.system(offcmd)
    if "--locker=lock" in sys.argv:
        if "lock" not in pslog:
            os.system("echo lock>>/tmp/pslog")
elif "--action=turnon" in sys.argv:
    if "off" in pslog:
        if "lock" not in pslog:
            os.system("echo on>/tmp/pslog")
            os.system(oncmd)
        elif "--locker=unlock" in sys.argv:
            os.system("echo on>/tmp/pslog")
            os.system(oncmd)
        else:
            os.system("touch /mnt/us/CantTurnOnIfLocked-screenpy")
elif "--action=switch" in sys.argv:
    if "on" in pslog:
        os.system("echo off>/tmp/pslog")
        os.system(offcmd)
    elif "off" in pslog:
        if "lock" not in pslog:
            os.system("echo on>/tmp/pslog")
            os.system(oncmd)
    else:
        os.system("touch /mnt/us/pslogCorrupted-screenpy")
else:
    os.system("touch /mnt/us/CommandMissing-screenpy")
