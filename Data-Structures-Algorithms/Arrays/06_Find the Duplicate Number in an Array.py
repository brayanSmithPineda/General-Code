# Find the Duplicate Number in an Array:

# Suppose there is exactly one duplicate number in the array, find that duplicate number.

#Brute force approach
def findDuplicateNumber(arr):
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if arr[i] == arr[j]:
                return arr[i]


arr = [1,2,2,3,5,4]
findDuplicateNumber(arr)
# output: 2

#Two Pointer Approach
def findDuplicateNumber(arr):
    left = 0
    for right in range(len(arr)):
        if arr[left] == arr[right]:
            return arr[left]
