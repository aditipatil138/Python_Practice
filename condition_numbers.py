def cond(num):
    sum = num[0]+num[1]
    diff = num[0]-num[1]
    if num[0]==num[1] or sum == 5 or diff == 5:
        return True
    else:
        return False
print(cond([2,3]))
print(cond([3,3]))
print(cond([12,13]))
print(cond([15,10]))