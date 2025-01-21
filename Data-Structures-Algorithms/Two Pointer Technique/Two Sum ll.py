# 4. Two Sum II (Input Array is Sorted)
# Problem: Given a sorted array of integers and a target value, find two numbers such that they add up to the target.

# Input: numbers = [2, 7, 11, 15], target = 9
# Output: [1, 2] (The numbers at index 1 and 2 add up to 9)

def twoSum(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return left,right
        elif current_sum < target:
            left += 1
        else:
            right -=1
    return "There is not two numbers that add up to the target"

numbers = [2, 7, 11, 15]
target = 9

twoSum(numbers,target)