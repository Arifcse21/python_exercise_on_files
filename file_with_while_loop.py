#! /usr/bin/env python3

file=open("file1.txt","r")

while True:
    data=file.read(1024)
    print(data)
    if not data:
        break



