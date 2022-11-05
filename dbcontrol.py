import os, sys, urllib.request, time, db

DB_URL = 'https://github.com/loh1na/demorepoforulinux/blob/main/database.db' 
# DATABASE AND PACKAGES CONFIGURATION
class Packages:
    def __init__(self, packages):
        self.packages = packages
    
    def Refresh_Mirrorlist(self):
        urllib.request.urlretrieve(DB_URL, "database.db")

    def Find_Package(self):
        for pkg in db.packages:
            #print (pkg)
            if pkg == self.packages:
                print (f"found package {self.packages}")
                return
                
