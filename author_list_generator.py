#! /usr/bin/env python3

list=[(1,'almasud','Abdullah Al Masud'),
      (2,'rimon','Rimol ALi'),
      (3,'Niloy','Niloy Roy'),
      (4,'sourov','Sourov Deb Sharma'),
      (5,'sathi','Sathi Rani Roy')]

with open("author_list.txt","w") as file:
    file.writelines("%d,%s,%s\n" %word for word in list)



