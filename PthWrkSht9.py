file1=open("C:/Users/17KBROWNE.acc/Downloads/10Random.txt", "r")
for line in file1:
    print(line)
    list0=line
list1=[]
for item in list0.split():
    list1.append(int(item))
list1.sort()