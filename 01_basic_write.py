#! /usr/bin/env python3

with open("author_list.txt","r") as f1:
    lists = f1.readlines()

with open("01_basic_write.txt","w") as file:
    for w in lists:
        file.writelines(w)







