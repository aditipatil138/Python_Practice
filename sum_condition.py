def sum(num):
    addition = num[0]+num[1]
    if 15 <= addition <= 20:
        return 20
    else:
        return addition
print(sum([2,3]))
print(sum([1,16]))
print(sum([12,3]))
print(sum([21,22]))