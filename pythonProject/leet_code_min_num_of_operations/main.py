# You are given a 0-indexed array nums consisting of positive integers.
#
# There are two types of operations that you can apply on the array any number of times:
#
# Choose two elements with equal values and delete them from the array.
# Choose three elements with equal values and delete them from the array.
#
# Return the minimum number of operations required to make the array empty, or -1 if it is not possible.

# case 1:
# Input: nums = [2,3,3,2,2,4,2,3,4]
# Output: 4
#
# case 2:
# Input: nums = [2,1,2,2,3,3]
# Output: -1
#
# case 3:
# input: nums = [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]
# output = 7

nums = [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]
nums.sort()

nums_set = set(dict.fromkeys(nums))
nums_list = list(nums_set)
nums_digits = []
operations = 0

# test to see if there are singular digits
for item in nums_set:
    if nums.count(item) != 1:
        nums_digits.append(nums.count(item))
    elif nums.count(item) == 1:
        operations = -1

if operations != -1:
    nums_dict = dict(zip(nums_list, nums_digits))
    print(nums_dict)
    for x, y in nums_dict.items():
        if y == 2:
            operations += 1
        elif y == 3:
            operations += 1
        elif y == 4:
            operations += 2
        elif y % 3 == 0:
            operations += y/3
        elif y % 3 == 1:
            operations += (((y - 1) / 3) + 1)
        elif y % 3 == 2:
            operations += (((y - 2) / 3) + 1)
print(int(operations))












