#Write a Python program to test whether a number is within 100 of 1000 or 2000.
number = int(input("Enter a number: "))
if 900 < number < 1100 or 1900 < number < 2100:
    print(True)
else:
    print(False)