import time
#Program to find out if numbers are higher or lower than each other
print("Let see if numbers are higher or lower than others")
time.sleep(1)
number1=float(input("Give me a number: "))
number2=float(input("Give me another number: "))
if ( number1 > number2 ):
    print(number1 ,"is higher than", number2)
elif ( number1 < number2 ):
    print(number1 ,"is lower than", number2)
else:
    print(number1, "and", number2," are equal")

#Program to find out if people can vote based on age
time.sleep(1)
print("Can you vote? Lets find out!")
time.sleep(1)
answer=int(input("How old are you? "))
if  ( answer >= 18 ):
    print("You can vote!")
else:
    print("You can't, moving on...")

#Program to find out if numbers are even or not
time.sleep(1)
print("Lets see if numbers are even...")
num=int(input("Enter a number:"))
if (num%2) == 0:
    print(num, "is even")
else:
    print(num, "is odd")

#Program to find out if numbers are divisible by 7
time.sleep(1)
print("Can numbers be divisible by 7, lets find out")
time.sleep(1)
num2=int(input("Enter a number: "))
if (num2%7) == 0:
    print(num2, "is divisible by 7")
else:
    print(num2, "isn't divisible by 7")

#Program to fint out if numbers are divisible by 5
time.sleep(1)
print("Lets play a game, if you enter a number divisible by five I'll say hello, if not I'll say bye. Okay lets play")
num3=int(input("Enter a number: "))
if (num3%5) == 0:
    print("Hello")
else:
    print("Bye")

#Program to calculate electricity bill
time.sleep(1)
unit=int(input("How many units of electricity do you have: "))
if unit>=200:
    print((unit-200)*10+500, "is the price")
elif unit<=100:
    print("No charge")
else:
    print((unit-100)*5, "is the price")

#Program to find out numbers first digits
time.sleep(1)
print("What are numbers first digits? Lets find out")
num4=int(input("Give me a number less than 3 digits: "))
if num4>=10:
    print("The first digit is", (num4//10))
else:
    print("The first digit is", num4)

#Program to find out if numbers last digits can be divisible by 3
time.sleep(1)
print("Can number's last digits be divisible by 3, lets find out")
time.sleep(1)
num5=int(input("Enter a two digit number: "))
if ((num5%10)%3) == 0:
    print(num5%10, "is divisible by 3")
else:
    print(num5%10, "isn't divisible by 3")
#Program to find out days of the week via numbers
time.sleep(1)
print("Lets guess days of the week via numbers")
num6=int(input("Give me a number between 1 and 7: "))
if num6==1:
    print("Sunday")
if num6==2:
    print("Monday")
if num6==3:
    print("Tuesday")
if num6==4:
    print("Wednesday")
if num6==5:
    print("Thursday")
if num6==6:
    print("Friday")
if num6==7:
    print("Saturday")

#Program to find out centigrade degrees in fahrenheit
time.sleep(1)
print("Lets convert from centigrade to fahrenheit")
cent=float(input("Enter a temperature in centigrade: "))
print(((9/5)*cent)+32, "is the temperature in fahrenheit")
time.sleep(1)

#Program to find out days of the week via Zellers Algorithm
print("Time to guess days of the week using Zellers algorithm")
c=int(input("Give me the first two numbers of the year: "))
y=int(input("Give me the last two numbers year: "))
dd=int(input("Give me the day of the month: "))
mm=int(input("Give me the month: "))
w=int((dd+((13*(mm+1))/5)+y+(y/4)+(c/4)-2*c)%7)
if w==0:
    print("Saturday")
if w==1:
    print("Sunday")
if w==2:
    print("Monday")
if w==3:
    print("Tuesday")
if w==4:
    print("Wednesday")
if w==5:
    print("Thursday")
if w==6:
    print("Friday")
