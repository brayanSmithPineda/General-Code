# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def twoSum(arr, target):
    hash_map = {}
    for index, element in enumerate(arr):
        diff =  target - element
        if diff in hash_map:
            return  hash_map[diff], index
        else:
            hash_map[element] = index

nums = [2,7,11,15]
target = 26
twoSum(nums, target)