# Two Sum Problem:

# Given an array of integers and an integer target, return indices of the two numbers such that they add up to the target.

arr = [1,4,2,3,6,7,5]

def twoSum(arr, target):
    arr.sort()
    left = 0
    right = len(arr)-1
    while left <= right:
        current_sum = arr[right] + arr[left]
        if current_sum == target:
            return right, left
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None
twoSum(arr,6)