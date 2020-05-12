#! /usr/bin/env python3

with open("03_basic_read.txt") as file:
    for line in file:
        s=line.split(",")
        print(s[0]+'-'+s[2])



