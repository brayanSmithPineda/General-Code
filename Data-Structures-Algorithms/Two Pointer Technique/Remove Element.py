# Remove Element: 
# Given an array and a value, remove all instances of that value in-place and return the new length of the array. Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

arr = [4,1,2,2,3,4,4,4,7,5,4]
value = 4
# out : length 6 arr = [1,2,2,3,7,5,,,]

#Objective: move all the element to the left
#We are going to have to pointer, one to mark the target value element(left), and a right pointer to loop through the array
#if we found a target element, then just right growth, remember left is design to track the target value
#if we found a not target element we move arr[right] to the left, in this case if left is dfferent from right we know for sure that we are going to replace that target value with the current one

def removeElement(arr,target):
    left = 0
    for right in range(len(arr)):
        if arr[right] != target:
            arr[left] = arr[right]
            left += 1
    return arr[:left], left

arr = [4,1,2,2,3,4,4,4,7,5,4]
value = 4

removeElement(arr,value)