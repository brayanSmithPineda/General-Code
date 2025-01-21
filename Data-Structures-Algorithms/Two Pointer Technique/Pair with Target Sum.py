# Pair with Target Sum:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. Assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1] (Because nums[0] + nums[1] == 9).

# We have to sum each item to know the sum, but here we can continually compare the sum of two elements, if the sum is greater than the target so we should move the left number, opposite the right, here we are using that the array is sorted so we know for sure were the target is going to be( left or right) if we compare it with the sum

#We initialize two pointer left = 0, and right = len(arr) - 1
# We loop through the arra until left <= right, we do not want to continue tracking the numbers we already did it
#if the sum of arr[left] + arr[right] > target, that means that we need to move right to the left, so the sum will get less.

def sumPairTarget(arr,target):
    left, right = 0, len(arr)-1
    while left <= right:
        sum = arr[left] +arr[right]
        if sum == target:
            return [left,right]
        elif sum > target:
            right -= 1
        elif sum < target:
            left += 1
    return 'Not Found'
nums = [2,7,11,15]
target = 17
sumPairTarget(nums,target)






def targetSum(arr,target):
    left,right  = 0 , len(arr)-1
    while left <= right:
        if arr[left]+arr[right] == target:
            return left,right
        elif arr[left]+arr[right] > target:
            right-=1
        elif arr[left]+arr[right] < target:
            left += 1
nums = [2,7,11,15]
target = 17
targetSum(nums,target)