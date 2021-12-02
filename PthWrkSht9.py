file1=open("C:/Users/17KBROWNE.acc/Downloads/10Random.txt", "r")
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
freq1=0
freq1list=[]
for i in range(len(list1)):
    freq1+=1
    if list1[i] == list1[i-1]:
        freq1+=1
    print(list1[i], "appears", freq1, "times")
    freq1list.append(freq1)
    freq1=0

file2=open("C:/Users/17KBROWNE.acc/Downloads/100Random.txt", "r")
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
freq1=0
for i in range(len(list1)):
    freq1+=1
    if list1[i] == list1[i-1]:
        freq1+=1
    print(list1[i], "appears", freq1, "times")
    freq1=0
