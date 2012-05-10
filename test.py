#!/mnt/us/python/bin/python2.6
for num in range(0,11):
    if num < 5:
        print str(num)+" smaller than 5"
        for k in range(1,11):
            if k < 5:
                print "k is smaller than 5 when k is "+str(k)
            elif k == 5:
                print "k is "+str(k)+"! Yeah!"
                break
            elif k > 5:
                print "k is larger than 5 when k is "+str(k)
    elif num == 5:
        print "It is "+str(num)+"! Yeah!"
    elif num > 5:
        print str(num)+" larger than 5"
        break
    else:
        print "What is this?"

