import time
file1=open("C:/Users/17KBROWNE.ACC/Downloads/10Random.txt", "r")
line1=file1.readline()
list1=[]
while line1 != "":
    list1.append(line1)
    print(line1, end = "")
    line1=file1.readline()
file1.close()
for [\n] in list1:
    list1.remove(\n)

time.sleep(1)

file2=open("C:/Users/17KBROWNE.ACC/Downloads/100Random.txt", "r")
line2=file2.readline()
list2=[]
while line2 != "":
    list2.append(line2)
    print(line2, end = "")
    line2=file2.readline()
file2.close()