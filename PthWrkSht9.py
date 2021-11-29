import time
file1=open("C:/Users/17KBROWNE.ACC/Downloads/10Random.txt", "r")
list1=[]
for line in file1:
    print(line)
    list1.append(line.strip())

time.sleep(1)
