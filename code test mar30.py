import math
#program1
num1= 2.1
num2= 3.6
print(num1)
print(num2)
print((num1+num2)/2, "is the average")
print(num1/num2, "is the remainder after division")
print(num2/num1, "is the remainder after division")
print(num1**num2, "is the first to the power of the second")

#program2
rad=float(input("Give me radius of cylinder"))
height=float(input("Give me height of cylinder"))
volume=math.pi*(rad**2)*height
print("Volume is", volume)

#program3
def str_comp():
    str1=str(input("Give me a string"))
    str2=str(input("Give me another string"))
    if str1 == str2:
        return True
    else:
        return False
print(str_comp())

#program4
number=int(input("Give me a number"))
for i in range(1, number):
    if i%2 != 0:
        print(i)

#program5
file1=open("Readme.txt", "r")
count=0
for line in file1:
    for ch in line:
        if ch == "a" or ch == "A":
            count=count+1
        elif ch == "e" or ch == "E":
            count=count+1
        elif ch == "i" or ch == "I":
            count=count+1
        elif ch == "o" or ch == "O":
            count=count+1
        elif ch == "u" or ch == "U":
            count=count+1
print(count, "is the number of vowels")

#program6
def addition(n):
    if n==0:
        return 0
    else:
        return n+addition(n-1)
print(addition(5))