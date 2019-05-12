import random

ans = int(input("What should the answer be? "))
if ans == -1:
    ans = random.randint(1, 100)
guess = int(input("How many guesses? "))
while guess > 0:
    g = int(input("Guess a number: "))
    if g == ans:
        print("You win!")
        break
    elif guess == 1:
        print("You lose; the number was " + str(ans) + ".")
    elif g < ans:
        print("The number is higher than that.")
    elif g > ans:
        print("The number is lower than that.")
    guess -= 1
