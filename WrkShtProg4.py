#print first 10 numbers
for i in range(1,11):
    print(i)

#print sum of even numbers from 10 to 20
for num in range(10,21,2):
    numlist=(range(10,21,2))
print(sum(numlist))

#print first 10 even numbers in reverse
for num0 in range(20,1,-2):
    print(num0)

#print square and cube of first ten numbers
for number in range(1,11):
    print(number**2 , number**3)

#print pattern based on user input
numbers=int(input("Give me a number please: "))
for number0 in range(1,numbers+1):
    for j in range(1,numbers+1):
        print("*")
    print("*")

#print product of 5 numbers from user
num1=int(input("Give me a number please: "))
num2=int(input("Give me another number please:  "))
num3=int(input("Give me another number please:   "))
num4=int(input("Give me another number please:  "))
num5=int(input("Give me another number please: "))
print(num1*num2*num3*num4*num5)