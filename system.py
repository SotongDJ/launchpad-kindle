#!/mnt/us/python/bin/python2.6
import sys
## -----------Change it if different---------
## ----------------------------------------------
o=open("/mnt/us/DK_System/xKindle/config.ini","a")
##cmd="/test/bin/usbnetwork"
##notif="/mnt/us/mplayer/mplayer /mnt/us/SLoDK/audio/usbNetworkTips.ogg"

if sys.argv[1] == "kindle":
    for line in open("/mnt/us/DK_System/xKindle/configbk").read().splitlines():
        if  "DefaultSystem" in line:
            o.write("DefaultSystem=3\n")
        else:
            line=line+"\n"
            o.write(line)
    o.close
if sys.argv[1] == "duokan":
    for line in open("/mnt/us/DK_System/xKindle/configbk").read().splitlines():
        if  "DefaultSystem" in line:
            o.write("DefaultSystem=1\n")
        else:
            line=line+"\n"
            o.write(line)
    o.close

##if sys.argv[1] == "usbnetwork":
##	os.system(cmd)
##	os.system(notif)

