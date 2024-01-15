# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


nums = [3,3]
target = 6

# print(nums[1:])

index = 1
first_num = 0
second_number = 0

for num in nums:
    additions = nums[index:]
    for num2 in additions:
        if num + num2 == target:
            # print(num, num2)
            first_num = num
            second_number = num2
            return_list = []
            return_list.append(nums.index(first_num))
            return_list.append(nums.index(second_number, index))
            print(return_list)


    index += 1
