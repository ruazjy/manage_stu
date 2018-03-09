import io
import print_stu


def index(file_path):
    while True:
        print u"please input the keyword that you want to sort,you can choose score/number/age"
        print u"if you want to break,please input quit!"
        keyword=raw_input(u"please input what you want:")
        if keyword=='quit':
            break
        elif keyword=='number':
            numbersort=sortstudent()
            numbersort.numbersort(file_path)
        elif keyword=='age':
            agesort=sortstudent()
            agesort.agesort(file_path)
        elif keyword=='score':
            scoresort=sortstudent()
            scoresort.scoresort(file_path)
        else:
            print u"please input correct keyword"

class sortstudent:
    def numbersort(self,file_path):
        read=io.io()
        information=[]
        information=read.read(information,file_path)
        sorted_information=sorted(information,key=lambda student:student[0])
        print_stu.printstudent(sorted_information)

    def agesort(self,file_path):
        read=io.io()
        information=[]
        information=read.read(information,file_path)
        sorted_information=sorted(information,key=lambda student:student[2])
        print_stu.printstudent(sorted_information)

    def scoresort(self,file_path):
        read=io.io()
        information=[]
        information=read.read(information,file_path)
        sorted_information=sorted(information,key=lambda student:student[3])
        print_stu.printstudent(sorted_information)

