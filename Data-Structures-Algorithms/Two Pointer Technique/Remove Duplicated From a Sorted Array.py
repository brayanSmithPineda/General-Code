# Remove Duplicates from Sorted Array:
# Given a sorted array, remove the duplicates in-place such that each element appears only once and return the new length. Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

# Example:
# Input: [1, 1, 3,4,4,5]
# Output: Length = 3, array becomes [1, 2,3].
#The key here is to have the unique values at the beggining of our array, the return the length
#We will have to find the unique elements, if we found one we move it to the left
#How do we find the unique element, as the list is sorted we can compare adjacent elements is they're different the element is unique
#To compare the adjacent element we are going to have two pointer

#We initilize a left pointer equal to 0 and the right equal to 1
#if the arr[left] != arr[right] that means is a unique element, so we move the element at the right to the left, and we increment left and right by 1
#if there is not unique element we just increment right

# Input: [1, 1, 3,4,4,4,5]
# Output: Length = 3, array becomes [1, 2,3].
def removeDuplicated(arr):
    left = 1
    for right in range(1,len(arr)):
        if arr[right] != arr[right-1]:
            arr[left] = arr[right]
            left += 1

    return left, arr[:left], arr
arr=[1, 2, 3,4,4,5]
removeDuplicated(arr)


#Check if the prior element = current, 
def removeDuplicates(arr):
    left = 1
    for right in range(1,len(arr)):
        if arr[right] != arr[right-1]:
            arr[left] = arr[right]
            left +=1
    return left , arr[:left], arr

arr = [1, 1, 3,4,4,4,5]
removeDuplicates(arr)