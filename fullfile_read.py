 #! /usr/bin/env python3

file=open("file1.txt","r")
data=file.readlines()  #read ALL the lines
print(data)            #readlines() returns a list
file.close()



