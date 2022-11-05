# info
Jabko is the minimal package manager for my linux distro called ULinux fully wrote on python

# How to run it
## WARNING: IT CAN HURT TO YOUR HOST SYSTEM BE SURE THAT YOU RUNNING ON VM OR SOMETHING LIKE
```
unzip Jabko-git-main.zip
cd Jabko-git-main
python main.py <option> <package>
```
# Options for jabko
### find
searches if package exists in database
example:
```
python main.py find nano
```

and if it exists it would wrote someting like this

![alt text](https://i.imgur.com/Wwd3mPS.png)

### install
installs and compiles package
example:
```
python main.py install nano
```

and it will install to default directory /bin
