#!/mnt/us/python/bin/python2.6
import os
import sys
os.system("touch /tmp/pslog")
offcmd="lipc-set-prop com.lab126.powerd preventScreenSaver 1"
oncmd="lipc-set-prop com.lab126.powerd preventScreenSaver 0"
pslog=open("/tmp/pslog").read().replace("\n","")
if sys.argv[-1] == "turnoff":
    if "off" not in pslog:
        os.system("echo off>/tmp/pslog")
        os.system(offcmd)
if sys.argv[-1] == "turnon":
    if "off" in pslog:
        os.system("echo on>/tmp/pslog")
        os.system(oncmd)
