# 3- Reverse an Array:

## Write a program to reverse the order of the elements in an array.

Algorithm

#Loop the array
#Have to pointer high and low
#Each time we assigned the new position we increment low and decrese high

def reverseArray(arr):
    return arr[::-1]

arr = [1,2,3,4,5]
reverseArray(arr)

def reverseTwoPointers(arr):
    left, right = 0, len(arr)-1
    while left<right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -=1
    return arr

arr = [1,2,3,4,5,6]
reverseTwoPointers(arr)
arr