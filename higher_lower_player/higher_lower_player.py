#Justin Cai, jc5pz

low = 1
high = 100
print("Think of a number between 1 and 100 and I'll guess it.")
guesses = int(input("How many guesses do I get? "))
while guesses > 0:
    guess = (low+high)//2
    r = input("Is the number higher, lower, or the same as " + str(guess) + "? ")
    if r == "same":
        print("I won!")
        break
    elif r == "higher":
        low = guess
    elif r == "lower":
        high = guess
    if guesses == 1:
        ans = int(input("I lost; what was the answer? "))
        if ans < low:
            print("That can't be; you said it was higher than " + str(low) + "!")
            break
        elif ans > high:
            print("That can't be; you said it was lower than " + str(high) + "!")
        else:
            print("Well played!")
    if low == high-1:
        print("Wait; how can it be both higher than " + str(low) + " and lower than " + str(high) + "?")
        break
    guesses -= 1
