import random
import math
a=int(input("Give a number:    "))
b=int(input("Give a lower number:    "))
random_choice = random.randint(a, b)
if a>b:
    upper=a
    lower=b
else:
    upper=b
    lower=a
min_number_guesses = round(math.log(upper - lower + 1, 2))
number_of_guesses = 0
while (number_of_guesses <= min_number_guesses):
    guess=int(input("Guess a number between them:   "))
    if guess == random_choice:
        print("Correct. That took you")
    else:
        print("You missed that one, try another!")