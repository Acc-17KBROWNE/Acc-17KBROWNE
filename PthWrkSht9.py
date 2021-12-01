file1=open("C:/Users/kpmbr_000/Downloads/10Random.txt", "r")
for line in file1:
    print(line)
    list0=line
list1=[]
for item in list0.split():
    list1.append(int(item))
list1==list1.sort()
range1=(list1[-1]-list1[0])
print("Range is", range1)
mean1=sum(list1)/10
print("Mean is", mean1)

file2=open("C:/Users/kpmbr_000/Downloads/100Random.txt", "r")
for line in file2:
    print(line)
    listo=line
list2=[]
for item in listo.split():
    list2.append(int(item))
list2==list2.sort()
range2=(list2[-1]-list2[0])
print("Range is", range1)
mean2=sum(list2)/10
print("Mean is", mean2)
