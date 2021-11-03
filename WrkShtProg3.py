import math
import random
a=int(input("Give a number:    "))
b=int(input("Give another number:    "))
if a>b:
    upper=a
    lower=b
else:
    upper=b
    lower=a
random_choice = random.randint(lower, upper)
max_number_guesses = round(math.log(upper - lower + 1, 2))
print ("You have a max of ", max_number_guesses, "guesses")
while (0 < max_number_guesses):
    guess=int(input("Guess a number between them:   "))
    number_of_guesses = max_number_guesses - 1
    if guess == random_choice:
        print("Correct.")
    else:
        print("You missed that one, try another!")
        max_number_guesses = max_number_guesses-1

#program to see if a credit card is valid
number=int(input("Please enter your credit card number, I promise I'm not sketchy:           "))
while number>0:
    odd=number%10
    number=number//10
    even_digit=number%10*2
    even=number%10*2
if even>9:
    while even>0:
        even_digit=even_digit+number%10
        number=number//10
else:
    even=even+even_digit
