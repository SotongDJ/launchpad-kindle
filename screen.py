#!/mnt/us/python/bin/python2.6
import os
import sys
os.system("touch /tmp/pslog")
cmd="if [ "$(lipc-get-prop com.lab126.powerd preventScreenSaver)" == "1" ]; then lipc-set-prop com.lab126.powerd preventScreenSaver 0; else lipc-set-prop com.lab126.powerd preventScreenSaver 1; fi"
## cmd="echo Success" # Juz for try
pslog=open("/tmp/pslog").read().replace("\n","")
if sys.argv[-1] == "on":
    if "true" not in pslog:
        os.system("echo true>/tmp/pslog")
        os.system(cmd)
if sys.argv[-1] == "off":
    if "true" in pslog:
        os.system("echo false>/tmp/pslog")
        os.system(cmd)
