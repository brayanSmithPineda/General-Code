"""
541. Reverse String II
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
"""

string = "brayan"

def reverse_string(string,k):
    char_to_list = list(string)
    
    for s in range(0,len(string),2*k):
        string[s:s+k] = reversed(string[s:s+k])

    return ''.join(char_to_list)

def reverseString(string, k):
    arr = list(string)
    for i in range(0,len(arr), 2*k):
        left, right = 0, min(i+k-1, len(arr)-1)
        while left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return ''.join(arr)