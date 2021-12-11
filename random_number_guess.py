import random

def number(x):
    random_number = random.randint(1,x)
    n = 0
    count = 1
    while n != random_number:
        
        n = int(input("Enter your Guess= "))
        if (n < random_number):
            print("Too low")
            count = count + 1
        elif (n > random_number):
            print("Too high")
            count = count + 1
    print("You guessed it!")
    print(f"You took {count} chances to guess the right number")
        
number(10)
