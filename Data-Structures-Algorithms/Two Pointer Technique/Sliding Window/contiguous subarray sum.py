"""
Problem Statement:
Given an array of integers nums and an integer k, your task is to find the total number of continuous subarrays whose sum equals k. (nums can have negative values)

Example 1:
Input: nums = [1, 1, 1], k = 2
Explanation: There are two subarrays that add up to 2: [1, 1] at indices 0 and 1, and [1, 1] at indices 1 and 2.
Output: 2
"""

def totalNumberSubarrays(arr, k):
    window_sum = 0
    left = 0
    count = 0
    for right in range(len(arr)):
        window_sum += arr[right]

        while window_sum > k:
            window_sum -= arr[left]
            left += 1
        
        if window_sum == k:
            count += 1
            window_sum -= arr[left]
            left += 1
    return count

nums = [1, 1, 1]
k = 2
totalNumberSubarrays(nums, k)