#!/mnt/us/python/bin/python2.6
import os
import sys
os.system("touch /tmp/pslog")
offcmd="lipc-set-prop com.lab126.powerd preventScreenSaver 1 "
oncmd="lipc-set-prop com.lab126.powerd preventScreenSaver 0 "
## "/mnt/us/mplayer/mplayer /mnt/us/SLoDK/audio/"
onNotif="/mnt/us/mplayer/mplayer /mnt/us/SLoDK/audio/autoScreensaverToggleOn.ogg"
offNotif="/mnt/us/mplayer/mplayer /mnt/us/SLoDK/audio/autoScreensaverToggleOff.ogg"
lockNotif="/mnt/us/mplayer/mplayer /mnt/us/SLoDK/audio/autoScreensaverToggleLock.ogg"
isLockNotif="/mnt/us/mplayer/mplayer /mnt/us/SLoDK/audio/screensaverCheckLook.ogg"
##
pslog=open("/tmp/pslog").read().replace("\n","")
if "--action=turnoff" in sys.argv:
    if "off" not in pslog:
        os.system("echo off>/tmp/pslog")
        os.system(offcmd)
        os.system(offNotif)
    if "--locker=lock" in sys.argv:
        if "lock" not in pslog:
            os.system("echo lock>>/tmp/pslog")
            os.system(lockNotif)
elif "--action=turnon" in sys.argv:
    if "off" in pslog:
        if "lock" not in pslog:
            os.system("echo on>/tmp/pslog")
            os.system(oncmd)
            os.system(onNotif)
        elif "--locker=unlock" in sys.argv:
            os.system("echo on>/tmp/pslog")
            os.system(oncmd)
            os.system(onNotif)
        else:
            os.system("touch /mnt/us/CantTurnOnIfLocked-screenpy")
            os.system(isLockNotif)
elif "--action=switch" in sys.argv:
    if "on" in pslog:
        os.system("echo off>/tmp/pslog")
        os.system(offcmd)
        os.system(offNotif)
    elif "off" in pslog:
        if "lock" not in pslog:
            os.system("echo on>/tmp/pslog")
            os.system(oncmd)
            os.system(onNotif)
        elif "lock" in pslog:
            os.system(isLockNotif)
    else:
        os.system("echo off>/tmp/pslog")
        os.system(offcmd)
else:
    os.system("touch /mnt/us/CommandMissing-screenpy")
