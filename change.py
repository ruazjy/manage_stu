import io

def index(file_path):
    while True:
        print u"please input student's number whose info you want to change"
        print u"if you want to break,please input quit!"
        keyword=raw_input(u"please input what you want:")
        if keyword=="quit":
            break
        else:
            changeline=change()
            changeline.changeinfo(keyword,file_path)

class change:
    def changeinfo(self,number,file_path):
        read=io.io()
        information=[]
        information=read.read(information,file_path)
        for i in information:
            if i[0]==number:
                print u"please input the student's information that you want to change like n:"
                keyword=raw_input(u"please input what you want:")
                keyword=keyword+'/n'
                information[information.index(i)]=keyword.split(" ")
        read.write(information,file_path)
