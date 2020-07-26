# This is a program that will get a name and add 'is cool' to the end
# Kevin McAleer
# Date: 26 July 2020

def coolify(name):
    return name + " is cool"

def __main__():
    myname = input("please type in your name: ")
    myname = coolify(myname)
    
    print(myname)
    