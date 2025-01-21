"""
344. Reverse String
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""
#This is the most efficient solution, O(N) time complexity and 0(1) space complexity
def reversedString(s):
    left, right = 0, len(s) - 1
    while left <= right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s
s = ["h","e","l","l","o"]
reversedString(s)


#We also can solve this with a stack, we just create a stack to store our data,we append each element of the list to the stack and then we pop the last and replace the original list. O(n) time and space complexity

def reversedStringStack(s):
    stack = []
    for i in s:
        stack.append(i)
    for j in range(len(s)):
        letter = stack.pop()
        s[j] = letter
    return s

s = ["h","e","l","l","o"]
reversedStringStack(s) 

#We can also solve this problem using recursion, is similar to the pointers approach, this is also O(n) space complexity, we do not use any extra data strcuture to store the list but as we recursively call the function we are using the call stack

def reversedStringRecursively(s, left = 0, right= None):
    if right is None: #We can not initlize right = len(s) -1 as an input so we just create a if stament to initilize it if it is equal to None
        right = len(s) -1
    if left >= right:
        return
    s[left], s[right] = s[right], s[left]
    reversedStringRecursively(s, left +1 , right -1)
s = ["h","e","l","l","o"]
reversedStringRecursively(s) 
