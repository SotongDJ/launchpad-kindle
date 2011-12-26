#!/mnt/us/python/bin/python2.6
import sys
test=open("/mnt/us/SotongDJ/test").read().replace("\n","")+"/"
tfile=open(test+"002-b-success.txt",'w')
tfile.write("yibi")
tfile.close()
