#! /usr/bin/env python3

authors=[[1,'almasud','Abdullah Al Masud'],
         [2,'rimon','Rimol Ali'],
         [3,'niloy','Niloy Roy'],
         [4,'sourov','Sourov Deb Sharma'],
         [5,'sathi','Sathi Rani Roy']
    ]

with open("02_basic_write.txt","w") as file:
    for w in authors:
        file.writelines(str(w))
        file.write("\n")




