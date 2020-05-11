try:
    with open("file1.txt") as file:
        for line in file:
            print(line)
except IOError:
    print("An IOError has occurred!")



#Without using "with" operator
#try:
#    file_handler = open("test.txt")
#    for line in file_handler:
#        print(line)
#except IOError:
#    print("An IOError has occurred!")
#finally:
#    file_handler.close()
#
