def printstudent(information):
    for i in information:
        print "number:%+20s" % str(i[0])
        print "name:%+20s" % str(i[1])
        print "age:%+20s" % str(i[2])
        print "score:%+20s" % str(i[3])
        print "address:%+20s" % str(i[4])

def selectstudent(num,information):
    for i in information:
        if i[0]==num:
            print "number:%+20s" % str(i[0])
            print "name:%+20s" % str(i[1])
            print "age:%+20s" % str(i[2])
            print "score:%+20s" % str(i[3])
            print "address:%+20s" % str(i[4])