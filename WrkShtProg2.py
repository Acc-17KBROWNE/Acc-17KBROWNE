import time
#Program to find out to find an average of 10 numbers

print("Please enter 10 numbers")
time.sleep(1)
Number1 = float(input("Enter Number 1 :"))
Number2 = float(input("Enter Number 2 :"))
Number3 = float(input("Enter Number 3 :"))
Number4 = float(input("Enter Number 4 :"))
Number5 = float(input("Enter Number 5 :"))
Number6 = float(input("Enter Number 6 :"))
Number7 = float(input("Enter Number 7 :"))
Number8 = float(input("Enter Number 8 :"))
Number9 = float(input("Enter Number 9 :"))
Number10 = float(input("Enter Number 10 :"))
sum = Number1 + Number2 + Number3 + Number4 +Number5 + Number6 + Number7 + Number8 + Number9 + Number10
print(sum/10, "is the average of these numbers")

#Program to print a multiplication table of 24

time.sleep(1)
a=int(input("Enter table number:"))
b=int(input("Enter the number that will table the table number:"))
i=1
while i<=b:
    print(a,"x",i,"=",a*i)
    i=i+1

#Program to convert from decimal to binary
import math
 
num=int(input("Enter a Number : "))
rem=""
while num>=1:
    rem+=str(num%2)
    num=math.floor(num/2)
 
binary=""
for i in range(len(rem)-1,-1,-1):
    binary = binary + rem[i]
    
print("The Binary format for given number is {0}".format(binary))

#Program to print out an infinite loop
time.sleep(10)
print("Wait for it")
time.sleep(10)
i=0
while i<=10:
    print("run")