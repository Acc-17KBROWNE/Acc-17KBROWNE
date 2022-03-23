def reading():
    filename=input("Give file name: ")
    word=1
    character=0
    line=0
    file1=open(filename,"r")
    myline = file1.readline()
    for ch in myline:
        character+=1
        if ch==" " or ch=="\n":
            word+=1
    while myline:
        print(myline)
        myline = file1.readline()
        for ch in myline:
            character+=1
            if ch==" " or ch=="\n":
                word+=1
        line+=1
    print(character, "is the amount of characters")
    print(line, "is the amount of lines")
    print(word, "is the amount of words")
reading()
