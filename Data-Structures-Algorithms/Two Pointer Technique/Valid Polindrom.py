# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Example:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true.

#Initialize two pointers at the left = 0 and right = len(arr) - 1
#Traverse the array with the pointer to the center comparing each alphanmeric caracter
#Problem: How to ignore characters that are not alphanumeric, that way i can compare just the import value

def validPolindrom(arr):
    left = 0
    right = len(arr)-1
    while left<=right:
        if not arr[left].isalnum():
            left+=1
        elif not arr[right].isalnum():
            right-=1
        else:
            if arr[left].lower() != arr[right].lower():
                return "It is not a polindrom"
            left +=1
            right -= 1
    return "It is a polindrom"

        

s = "A man, a plan, a canal: Panama"
validPolindrom(s)