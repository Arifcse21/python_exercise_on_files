#! /usr/bin/env python3

with open("03_basic_read.txt") as file:
    for line in file:
        word=line.split(",")
        print(word)



