# Question 16(a)
# Name and School: Kevin Browne, Athlone Community College

file1=open("shelley.txt", "r")
list1=[]
list2=[]
count=0
for line in file1:
    list1.append(line)
print("The poem has been correctly read by the program")
print("The last line is: '", list1[-1], "'")
for i in list1:
    count+=1