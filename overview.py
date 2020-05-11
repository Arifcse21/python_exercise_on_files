#! /usr/bin/env python3

file= open("file3.txt","w+")
#f=open("file3.txt","a+")
for i in range(10):
    file.write("This is line %d\r\n" % (i+1))
file.close()
#Open the file back and read the contents
#file=open("file3.txt", "r")
#if file.mode == 'r':
#   data =file.read()
#    print (data)
#readlines reads the individual line into a list
#data =file.readlines()
#for x in data:
#print(x)



