# 219. Contains Duplicate II

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true

def duplicates(arr, k):
    left = 0
    for right in range(1, len(arr)):
        if arr[left] == arr[right] and abs(left - right) <= k:
            return True
        else:
            right += 1
    return False

nums = [1,2,3,1,2,3]
k = 2

duplicates(nums, k)

abs(0)