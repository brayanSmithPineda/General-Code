# Problem: Given a string, reverse it using the two-pointer technique.
# Example:

# Input: "hello"
# Output: "olleh"

def reverseString(string):
    left = 0
    right = len(string)-1

    string = list(string)
    while left <= right:
        string[left], string[right] = string[right], string[left]
        left += 1
        right -= 1
    return ''.join(string)

string = "hello"
reverseString(string)

# 2. Valid Palindrome
# Example:

# Input: "A man, a plan, a canal: Panama"
# Output: True (Ignoring non-alphanumeric characters and case, it reads the same forward and backward)

def validPalindrome(s):
    left, right = 0, len(s)-1
    while left <= right:
        if s[left].isalnum() == False:
            left += 1
        elif s[right].isalnum() == False:
            right -= 1
        else:
            if s[left].lower() != s[right].lower():
                return "Not a Palindrom"
            left += 1
            right -= 1
    return "It is a Palindrome"

s = "A man, a plan, a canal: Panama"
validPalindrome(s)

#3. Merge Two Sorted Arrays
# Problem: Given two sorted arrays, merge them into a single sorted array.
# Example:

# Input: arr1 = [1, 3, 5, 0, 0, 0], m = 3 n = 3 arr2 = [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]

#We need two pointer first one at arr1 that point to the las poisition of the actual array
# we need a second pointer that point at the las position of arr2
# we need a variable that stores the position of the last element of arr1
# The idea here is to compare each last element of arr1 and arr2 and the largest put it in the las element of arr1 and so on

def mergeTwoSortedArray(arr1,arr2,m,n):
    last = m + n - 1
    while m > 0 and n > 0:
        if arr1[m - 1] > arr2[n - 1]:
            arr1[last] = arr1[m - 1]
            last -= 1
            m -= 1
        elif arr1[m - 1] < arr2[n - 1]:
            arr1[last] = arr2[n -1]
            last -= 1
            n -= 1
    while n>0:
        arr1[last] = arr2[n-1]
        n -= 1
        last -= 1 
    return arr1
arr1 = [2, 3, 5, 0, 0, 0]
m = 3 
n = 3 
arr2 = [1, 4, 6]

mergeTwoSortedArray(arr1,arr2,m,n)