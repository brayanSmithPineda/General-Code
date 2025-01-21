# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2

#The key is here is to notice that the list was sorted at some point, so we have a list with two parts that are sorted, and well-known O(logn) algorithm to find an element is a Binary search algorithm, so what we need to do is perform a binary seach with a twist that appliad to this problem

#First we need to know that we can not perform Binary Search as usual, since the entire list is not sorted, so you can have the target in both parts left an right
"""
nums = [4,5,6,7,0,1,2]
left = 0
right = len(nums) - 1
mid = 7
target = 0

in this case is you perfom Binary search as usual your going to say that mid > target so you update the right pointer and look at the left for the target, which is incorrect because the target is at the left. 
"""

#So to perform the Binary search you first need to know in which part of the list are you in, the right sorted part or the left sorted part (remember that as the array was sorted there are two parts that are sorted)

#One you identify where the mid point is, let's say the left part, you can check if the target is between the left and the middle, you update the right pointer and perform binary seach, if its not that means is at the right so you update the left pointer. Is the same if the mid point is at the right part

def searchInsertPosition(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        #Check if we are in the left sorted portion of the array, perform binary search on that side
        if nums[mid] > nums[right]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        #We are in the right sorted portion of the array, perform binary search on that side
        if nums[mid] < nums[right]:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        

nums = [4,5,6,7,0,1,2]
target = 0

searchInsertPosition(nums,target)