import io
def index(file_path):
    while True:
           print u"please input the number student's that you want to delete"
           print u"if you want to break,please input quit"
           keyword=raw_input(u"please input what you want:")
           if keyword=='quit':
               break
           else:
               deleteline=delete()
               deleteline.deleteinfo(keyword,file_path)

class delete:
    def __init__(self):
        print u"we will delete the student's info"
    def deleteinfo(self,number,file_path):
        read=io.io()
        information=[]
        information=read.read(information,file_path)
        for i in information:
            if i[0]==number:
                information.remove(i)
        read.write(information,file_path)