#! /usr/bin/env python3

file=open("file2.txt","w")
file.write("This is line is writen first!\n")
file.close()

file=open("file2.txt","a")
file.write("This line is appended!")
file.close()

file=open("file2.txt","r")
for line in file:
    print(line)
file.close()



