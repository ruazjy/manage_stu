import io
import print_stu

def index(file_path):
    while True:
        print u"please input the student's number who you want to select"
        print u"if you want to break,please input quit!"
        keyword=raw_input(u"please input what you want:")
        if keyword=="quit":
            break
        else:
            selectline=select()
            selectline.selectinfo(keyword,file_path)

class select:
    def selectinfo(self,number,file_path):
        read=io.io()
        information=[]
        information=read.read(information,file_path)
        print_stu.selectstudent(number,information)


