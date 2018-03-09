import io
def index(file_path):
    while True:
        print u'please input a student information like;number name age score address'
        print u'if you want to break,please input quit!'
        keyword=raw_input(u'please input what you want:')
        if keyword=='quit':
            break
        else:
            addline=add()
            addline.addinfo(keyword.split(" "),file_path)

class add:
    def __init__(self):
        print u"we will input this student's information"

    def addinfo(self,student,file_path):
        read=io.io()
        read.add(student,file_path)