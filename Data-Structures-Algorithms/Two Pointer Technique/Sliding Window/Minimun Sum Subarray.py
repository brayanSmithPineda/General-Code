"""
209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""

#Objective: Traverse the arr with two pointers and look for the subarray that is >= target, and save it length in a curent_length

def minumSizeInnerLoop(arr, target):
    left = 0
    window_sum = 0
    result = float("inf")
    for right in range(len(arr)):
        window_sum += arr[right]

        while window_sum >= target and left < len(arr):
            result = min(result, right - left + 1)
            window_sum -= arr[left]
            left += 1
    return result

#The foor loop is goint to be our right pointer, the scenarios wheren the window sum is greter than the target and when is equal to the target is handle with the inne while loop, the outer while loop handles the scenario the is less than the target

nums = [1,2,3,4,5]
target = 11
minumSizeInnerLoop(nums, target)

def minimunSizeSubarray(arr, target):
    left = 0
    right = 0
    global_len = float('inf')
    window_sum = arr[0]
    while left < len(arr) and right < len(arr):
        if window_sum < target:
            right += 1
            if right < len(arr):
                window_sum += arr[right]
        elif window_sum > target:
            global_len = min(global_len, len(arr[left:right+1]))
            window_sum -= arr[left]
            left += 1
        elif window_sum == target:
            global_len = min(global_len, len(arr[left:right+1]))
            right += 1
            if right < len(arr):
                window_sum = window_sum + arr[right] - arr[left]
            left += 1
    return global_len if global_len != float('inf') else 0

nums = [1,2,3,4,5]
target = 11
minimunSizeSubarray(nums, target)

