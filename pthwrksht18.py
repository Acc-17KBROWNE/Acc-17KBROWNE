#Program 1

list1=[]
def large(list1):
    check=0
    number=int(input("How many numbers would you like to add to list? "))
    for i in range(0, number):
        list1.append(int(input("Add number: ")))
    for i in range(len(list1)):
        if list1[i]>check:
            check=list1[i]
    print(check)
large(list1)

#Program 2

list2=[]
def reverse(list2):
    number=int(input("How many numbers would you like to add to list? "))
    for i in range(0, number):
        list2.append(int(input("Add number: ")))
    list2.reverse()
    print(list2)
reverse(list2)

#Program 3

list3=[]
def checker():
    number=int(input("How many numbers would you like to add to list? "))
    for i in range(0, number):
        list3.append(int(input("Add number: ")))
    check=int(input("What number would you like to check for? "))
    if check in list3:
        print("Yes :)")
    else:
        print("No :(")
checker()

#Program 4

list4=[]
def odder():
    listo=[]
    number=int(input("How many numbers would you like to add to list? "))
    for i in range(0, number):
        list4.append(int(input("Add number: ")))
    for i in range(len(list4)):
        if i%2==0:
            listo.append(list4[i])
    print(listo)
odder()

#Program 5

list5=[]
def runningtotal():
    number=int(input("How many numbers would you like to add to list? "))
    for i in range(0, number):
        list5.append(int(input("Add number: ")))
    print(sum(list5), "is the running total")
runningtotal()

#Program 6

def palindrome():
    palin=True
    string1=str(input("Enter string: "))
    for i in range(len(string1)):
        if string1[i]!=string1[-(1+i)]:
            palin=False
            break
    if palin==True:
        print("Yes it is palindrome")
    else:
        print("no")
palindrome()

#Program 7

list7=[]
number=int(input("How many numbers would you like to add to list? "))
for i in range(0, number):
    list7.append(int(input("Add number: ")))
def forsum():
    numo1=0
    for i in list7:
        numo1=numo1+i
        return numo1
forsum()

def whilesum():
    i=0
    numo2=0
    while i<len(list7):
        numo2=numo2+list7[i]
        i+=1
        return numo2
whilesum()

def recursum(list7):
    if len(list7)==1:
        return list7[0]
    else:
        return list7[0]+recursum(list7[1:])
print(recursum(list7))

#Program 8

def perfect_square():
    square=int(input("What number would you like to go up to? "))
    for i in range(1, square+1):
        print(i*i)
perfect_square()

#Program 9

list0=[]
number=int(input("How many numbers would you like to add to list? "))
for i in range(0, number):
    list0.append(int(input("Add number: ")))
listo=[]
number=int(input("How many numbers would you like to add to list? "))
for i in range(0, number):
    listo.append(int(input("Add number: ")))
list0.extend(listo)
print(list0)

#Program 10

list0=[]
number=int(input("How many numbers would you like to add to list? "))
for i in range(0, number):
    list0.append(int(input("Add number: ")))
listo=[]
number=int(input("How many numbers would you like to add to list? "))
for i in range(0, number):
    listo.append(int(input("Add number: ")))
for i in range(len(listo)):
    list0.insert(list0[i], listo[i])
print(list0)

#Program 11

list0=[]
number=int(input("How many numbers would you like to add to list? "))
for i in range(0, number):
    list0.append(int(input("Add number: ")))
listo=[]
number=int(input("How many numbers would you like to add to list? "))
for i in range(0, number):
    listo.append(int(input("Add number: ")))
list0.extend(listo)
list0.sort()
print(list0)