# Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
def sum(num1, num2, num3):
    sum = num1 + num2 + num3
    if num1 == num2 == num3:
        return sum*3
    else:
        return sum
print(sum(2,2,2))
print(sum(3,5,6)) 