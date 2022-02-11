import random
#Program 1

print("Hello World")

#Program 2+3

name=str(input("Give your name: "))
if name == "Alice":
    print("Good Morning", name)
if name == "Bob":
    print("Good Morning", name)
else:
    print("Good Morning")

#Program 4+5

num=int(input("give num :   "))
sumo=0
for i in range(1, num):
    if i%5==0 or i%3==0:
        sumo=sumo+i
print(sumo)

#Program 6

num=int(input("give num :   "))
sumo=0
choice=int(input("Type 1 for sum, type 2 for product: "))
if choice==1:
    for i in range(1, num):
        sumo=sumo+i
    print(sumo)
if choice==2:
    sumo=1
    for i in range(1, num):
        sumo=sumo*i
    print(sumo)
else:
    print("noperino")

#Program 7

num=int(input("Give num between 1 and 12:         "))
for i in range(1, 13):
    print(num, "x", i, "=", num*i)

#Program 8

for n in range(1, 101):
    if n>1:
        for i in range(2, n):
            if n%i==0:
                break
        else:
            print(n)

#Program 9

num1=int(input("give small num :   "))
num2=int(input("give big num :   "))
number=random.randint(num1, num2)
guess=int(input("Guess secret number:                        "))
guesses=1
while number!= "guess":
    if guess<number:
        print("Too Low")
        guess=int(input("Guess secret number:                        "))
        guesses+=1
    elif guess>number:
        print("Too High")
        guess=int(input("Guess secret number:                        "))
        guesses+=1
    else:
        print("You got it superstar! :) In", guesses, "guesses!")
        break

#Program 10
year=2022
for i in range(0, 20):
    print(year + i*4)