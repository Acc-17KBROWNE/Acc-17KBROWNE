import statistics
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
freq1list={}
for i in list1:
    if i in freq1list:
        freq1list[i] +=1
    else:
        freq1list[i] =1
print(freq1list)
mode1=statistics.mode(list1)
print(mode1, "is the mode")
median1=statistics.median(list1)
print(median1, "is the median")

file2=open("C:/Users/17KBROWNE.acc/Downloads/100Random.txt", "r")
list2=[]
for line in file2:
    print(line)
    for item in line.split():
        list2.append(int(item))
list2==list2.sort()
range2=(list2[-1]-list2[0])
print("Range is", range2)
mean2=sum(list2)/10
print("Mean is", mean2)
freq2list={}
for i in list2:
    if i in freq2list:
        freq2list[i] +=1
    else:
        freq2list[i] =1
print(freq2list)
mode2=statistics.mode(list2)
print(mode2, "is the mode")
median2=statistics.median(list2)
print(median2, "is the median")

file3=open("results.txt", "w")
file3.write(freq1list)
file3.write("Mode:", mode1)
file3.write("Median:", median)
file3.write("Mean:", mean1)
file3.write("Range:", range1)
file3.write("Mode:", mode1)
file3.write("Median:", median)
file3.write("Mean:", mean1)
file3.write("Range:", range1)
