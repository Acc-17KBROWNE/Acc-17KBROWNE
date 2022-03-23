def reading():
    filename=input("Give file name: ")
    word=0
    character=0
    line=0
    file1=open(filename,"r")
    for line in file1:
        print(file1.readline())
reading()