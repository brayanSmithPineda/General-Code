"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
"""

def longestSubstring(string):
    max_count = 0
    hashmap = {}
    left = 0
    for right in range(len(string)):
        if string[right] in hashmap:
            left = max(left, hashmap[string[right]] + 1)
        hashmap[string[right]] = right

        max_count = max(max_count, right - left + 1)
    return max_count
s = "abcabcbb"
longestSubstring(s)

def longestSubstring(string):
    max_count = 0
    hashmap = {}
    left = 0
    for right in range(len(string)):
        while string[left] != string[right]:
            left += 1
        hashmap[string[right]] = right

        max_count = max(max_count, right - left + 1)
    return max_count