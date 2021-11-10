import time
#print first 10 numbers
for i in range(1,11):
    print(i)

time.sleep(1)
#print sum of even numbers from 10 to 20
for num in range(10,21,2):
    numlist=(range(10,21,2))
print(sum(numlist))

time.sleep(1)
#print first 10 even numbers in reverse
for num0 in range(20,1,-2):
    print(num0)

time.sleep(1)
#print square and cube of first ten numbers
for number in range(1,11):
    print(number**2 , number**3)

time.sleep(1)
#print pattern based on user input
numbers=int(input("Give me a number please: "))
for number0 in range(1,numbers+1):
    for j in range(1,numbers+1):
        print("*")
    print(" ")

time.sleep(1)
#print product of 5 numbers from user
num1=int(input("Give me number pls: "))
num2=int(input("Give me number pls: "))
num3=int(input("Give me number pls: "))
num4=int(input("Give me number pls: "))
num5=int(input("Give me number pls: "))
print("The last number will be the product of those numbers")
time.sleep(1)
for x in range((num1*num2*num3*num4*num5)+1):
    print(x)
