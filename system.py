#!/mnt/us/python/bin/python2.6
import sys
## -----------Change it if different---------
## ----------------------------------------------
o=open("/mnt/us/DK_System/Lite/config.ini","a")
if sys.argv[1] == "kindle":
	for line in open("/mnt/us/DK_System/Lite/configbk").read().splitlines():
		if  "DefaultSystem" in line:
			o.write("DefaultSystem=3\n")
		else:
			line=line+"\n"
			o.write(line)
	o.close
if sys.argv[1] == "duokan":
	for line in open("/mnt/us/DK_System/Lite/configbk").read().splitlines():
		if  "DefaultSystem" in line:
			o.write("DefaultSystem=1\n")
		else:
			line=line+"\n"
			o.write(line)
	o.close
