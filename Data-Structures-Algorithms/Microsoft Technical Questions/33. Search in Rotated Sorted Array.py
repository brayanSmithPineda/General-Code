"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""

#As we know the algorithm was previouly sorted, now after the rotation, the nums list contains two parts, the right part that it is sorted itsefl, and the left part that its also sorted, we can perform Binary Search with a twist to find the position of the target number which is a well-known O(logn) algorithm
#We can not use Binary search as usual because the entire list its not sorted so if the target is less than the mid we can not move right or left because the target could be at any of both directions.
#So what we could do is first identify in which part the mid is, if it is and the right sorted portion, then we can see if mid < target < right, if that is true that means the target is at the right so we just move the left pointer to mid + 1, else means the target is at the left, so we set right = mid -1, we do something similar if mid is at the left sorted portion of the list

def rotated_sorted_array(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[mid] <= nums[right]: #This means we are at right-sorted portion
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else: 
                right = mid - 1
        
        if nums[mid] > nums[right]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1 

nums = [1]
target = 1
rotated_sorted_array(nums, target)