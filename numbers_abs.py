# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
given_number = int(input("Enter a number: "))
if given_number > 17: 
    print((given_number-17)*2)
else: 
    print(17-given_number)
    