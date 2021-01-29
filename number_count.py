def number_count(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1
    return count
print(number_count([1,2,4,3,4,2,5 ]))
print(number_count([4,4,4,4,4,5,5,4,5,4,5,4]))
