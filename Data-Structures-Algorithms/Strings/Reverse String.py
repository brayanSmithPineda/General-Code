"""
Write a function that reverses a string. The input string is given as an array of characters s. You must do this by modifying the input array in-place with O(1) extra memory.
"""
def reverseString(string):
    return string[::-1]

string = 'brayan'
reverseString(string)

#Slicing always create a new object, so it is not an in place operation
id(string)
id(string[::-1])

#use to pointer to swap the elements

def reverse_strin(string):
    left, right = 0, len(string) - 1
    arr = list(string)
    while left <= right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return ''.join(arr)
string = 'brayan'
reverse_strin(string)