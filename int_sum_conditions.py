def number(num):
    if num[0]==num[1] or num[1]==num[2] or num[0]==num[2]:
        return 0
    else:
        sum = num[0]+num[1]+num[2]
        return sum
print(number([1,2,3]))
print(number([2,2,3]))
print(number([8,2,5]))