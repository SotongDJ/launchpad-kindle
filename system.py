#!/mnt/us/python/bin/python2.6
import sys
import os
## -----------Change it if different---------
## ----------------------------------------------
##cmd="/test/bin/usbnetwork"
##notif="/mnt/us/mplayer/mplayer /mnt/us/SLoDK/audio/usbNetworkTips.ogg"

if sys.argv[1] == "kindle":
    o=open("/mnt/us/DK_System/xKindle/config.ini","a")
    for line in open("/mnt/us/DK_System/xKindle/configbk").read().splitlines():
        if  "DefaultSystem" in line:
            o.write("DefaultSystem=3\n")
        else:
            line=line+"\n"
            o.write(line)
    o.close
if sys.argv[1] == "duokan":
    o=open("/mnt/us/DK_System/xKindle/config.ini","a")
    for line in open("/mnt/us/DK_System/xKindle/configbk").read().splitlines():
        if  "DefaultSystem" in line:
            o.write("DefaultSystem=1\n")
        else:
            line=line+"\n"
            o.write(line)
    o.close

if sys.argv[1] == "chkip":
    os.system("ifconfig wlan0>/tmp/iptmp") #for kindle
#    os.system("ifconfig wlan1>/tmp/iptmp") #for my desktop
    datasets=[]
    tmpset=[]
    ip=''
    datasets=open("/tmp/iptmp").read().splitlines()
    for dataset in datasets:
        tmpset=tmpset+dataset.split(" ")
    for data in tmpset:
        if "addr:" in data:
            ip=data.replace("addr:","")
            #print ip
            for a in ip:
                #print a
                os.system("/mnt/us/mplayer/mplayer /mnt/us/SLoDK/audio/num"+a+".ogg")
##
##
##if sys.argv[1] == "usbnetwork":
##	os.system(cmd)
##	os.system(notif)

