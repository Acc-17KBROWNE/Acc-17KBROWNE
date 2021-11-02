import random
a=int(input("Give a number:    "))
b=int(input("Give a lower number:    "))
random_choice = random.randint(a, b)
if a>b:
    upper=a
    lower=b
else:
    upper=b
    lower=a
max_number_guesses =(upper - lower + 1)
print ("You have a max of ", max_number_guesses, "guesses")
while (0 < max_number_guesses):
    guess=int(input("Guess a number between them:   "))
    number_of_guesses = max_number_guesses - 1
    if guess == random_choice:
        print("Correct. That took you", max_number_guesses - number_of_guesses, "guesses")
    else:
        print("You missed that one, try another!")
        max_number_guesses-1
