import add
import delete
import change
import select
import sort

file_path='student.txt'

def main():
        while True:
            print u'welcom to student information management system!'
            print u'you can use input:add;delete;change;select;sort;quit'
            keyword=raw_input("please input what you want to operation:")
            if keyword=='quit':
                exit(0)
            elif keyword=='add':
                add.index(file_path)
            elif keyword=='delete':
                delete.index(file_path)
            elif keyword=='change':
                change.index(file_path)
            elif keyword=='select':
                select.index(file_path)
            elif keyword=='sort':
                sort.index(file_path)
            else:
                print u'please input correct option!'

if __name__=='__main__':
    main()