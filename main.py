import time, os, urllib.request, sys, tarfile, re
#importing custom files
import dbcontrol, db
#some variables
path = os.getcwd()

class main:
    def __init__(self, arg):
        self.arg = arg

    def Find_package(self):
        db = dbcontrol.Packages(self.arg)
        db.Find_Package()
    def Install_package(self):
        dbd = db.packages
        for inp in dbd:
            if inp == self.arg:
                try:
                    print(f"begining of instalation package {self.arg}")
                    urllib.request.urlretrieve(dbd[self.arg], 'package.tar.xz')
                    print (f"downloaded package {self.arg}")
                    print (f"unpacking package {self.arg}")
                    with tarfile.open('package.tar.xz', "r:xz") as inst:
                        inst.extractall(path=".")
                        print (f"package {self.arg} extracted!")
                        print ("entering the directory...")
                        for root, dirs, files in os.walk('.', topdown=False):
                            for name in dirs:
                                if name.find(self.arg) != -1:
                                    os.chdir(name)
                                    print ("compiling and installing package...")
                                    if name.find("Makefile") != -1:
                                        os.system("make -j{os.cpu_count()}")
                                    else:
                                        os.system(f"./configure --prefix=/usr && make -j{os.cpu_count()}")
                                        print ("instalation finished")
                        inst.close()
                    remo = os.path.join(path, 'package.tar.xz')
                    os.remove(remo)
                    return
                except KeyboardInterrupt:
                    print("canceling procces of instalation...")
                    return
        print(f"package {self.arg} not found!")


        


if __name__ == '__main__':
    try:
        Main = main(sys.argv[2])
        if sys.argv[1] == 'find':
            Main.Find_package()
        if sys.argv[1] == 'install':
            Main.Install_package()
    except IndexError:
        print("additional arguments requied")


        
