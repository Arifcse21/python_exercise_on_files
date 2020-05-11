#! /usr/bin/env python3

with open("file1.txt") as file:    #no mode needed
    for line in file:
        print(line)

#by using "with" operator file closing is also not needed.




