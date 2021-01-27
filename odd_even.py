#Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
number = int(input("Enter a Integer number to check if it is even or odd: "))
if number%2==0:
    print("The number {} is Even".format(number))
else:
    print("The number {} is Odd".format(number))