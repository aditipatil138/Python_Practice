def number_check(number_list, number):
    for value in number_list:
        if value == number:
           return True
    return False
print(number_check([1,5,8,3], 3))
print(number_check([1,5,8,3], -1))