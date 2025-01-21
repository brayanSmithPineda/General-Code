"""
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""

#Kadane's Algorithm
#1 - Intilize two variable, current_sum y gobal_sum, current_sum is going to keep track of the current sum of the subarray, and gobal sum is going to be the the largest sum of those current sums
#2- the key here is to compare the current element with the previous sum and choose the largest one 

def kadanesAlgorithm(arr):
    current_sum = global_sum = arr[0]
    for i in range(len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        if current_sum > global_sum:
            global_sum = current_sum
    return global_sum 




"""

2. Sliding Window Problems

Longest Substring Without Repeating Characters: Find the length of the longest substring without repeating characters.
Substring with Concatenation of All Words: Find all starting indices of substring(s) in a given string that is a concatenation of each word in a list exactly once.
Permutation in String: Check if a string's permutations are a substring of another string.
Sliding Window Maximum: Find the maximum value in each sliding window of size k.
Longest Repeating Character Replacement: Find the length of the longest substring that can be obtained by replacing no more than k characters.
Fruit Into Baskets: In a row of trees, each tree has a fruit type. You can start at any tree and move to the right, but you can't pick more fruits than your baskets can hold. What is the maximum number of fruits you can collect?
Sliding Window Median: Find the median of the element inside the window at each moving.
Longest Substring with At Most K Distinct Characters: Find the length of the longest substring that contains at most k distinct characters.

"""