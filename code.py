import random

number = random.randint(1,9)
chances = 0


while chances<5:
    guess = int(input("Guess any number between 1 and 9: "))

    if guess == number:
        print("That's right :)")
        break
    
    elif guess < number:
        print("That's lower than the number :( ")

    else:
        print("That's higher than the number :( ")
    
    chances+=1

if chances==5:
    print("Oops, maximum chances reached")