class io:
    def read(self,information,file_path):
        with open(file_path,'r') as f:
            for line in f:
                information.append(line.split(' '))
        return information

    def write(self,information,file_path):
        f=open(file_path,'w')
        for line in information:
            f.write(' '.join(line))
        f.close()

    def add(self,information,file_path):
        f=open(file_path,'a')
        print>>f,' '.join(information)
        f.close()

