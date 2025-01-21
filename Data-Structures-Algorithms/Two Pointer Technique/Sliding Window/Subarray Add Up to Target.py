"""
Given an array of positive integers, find the subarrays that add up to a given number
input: example = [8,7,4,3,1,2,1,5,1] target = 7
outpu: 7, [4,3], [1,5,1]
"""
# Objective: Create a dynamic sliding window to traverse the array, shrink or expand the window based on the sum of the elements of the subarray, if the subarray is less than the target then expand the window, greater shrink the window, equal to the target then save the subarray in a variable that store the subarray
#--- Creater a variable to store the result
#--- To traverse the array we are going to use a while loop with a left and right pointer, left and right will be initilize at cero
#--- Compare the window_sum = arr[right] + arr[left] with the target, if its greater updated left by one, if its less than target then updated right by one. Key: we have to create a special case when left = right, in those cases we can not calculate the window sum as arr[right] + arr[left] because we would be duplicated the sum
def subarray_addup_togivenNumber(arr, target):
    left = 0
    window_sum = 0
    result = []
    for right in range(len(arr)):
        window_sum += arr[right]
        while window_sum > target:
            window_sum -= arr[left]
            left += 1
        if window_sum == target:
            result.append(arr[left:right+1])
            window_sum -= arr[left]
            left += 1
    return result

arr = [3, 3 ,3,2,1]
target = 3
subarray_addup_togivenNumber(arr, target)


def subarray_target_sum(arr, target):
    res = []
    left, right = 0, 0
    window_sum = arr[0]
    while left < len(arr) and right < len(arr):
        if window_sum == target:
            res.append(arr[left:right+1])
            right += 1
            if right < len(arr) and left < len(arr):
                window_sum = window_sum - arr[left] + arr[right]
            left += 1
        elif window_sum < target:
            right += 1
            if right < len(arr):
                window_sum = window_sum + arr[right]
        elif window_sum > target:
            window_sum = window_sum - arr[left]
            left += 1
    return res

arr = [3, 3 ,3,2,1]
target = 3
subarray_target_sum(arr, target)

arr = [0,1,2,5,2]
target = 7
subarray_target_sum(arr, target)

arr = [7,1,2,3,4]
target = 7
subarray_target_sum(arr, target)

def subarray_target_sum(arr, target):
    res = []
    left, right = 0, 0
    window_sum = 0
    
    while right < len(arr):
        # Add the rightmost element to the window sum
        window_sum += arr[right]
        
        # Shrink the window from the left if the sum exceeds the target or if left equals right (avoid empty subarray)
        while window_sum > target and left <= right:
            window_sum -= arr[left]
            left += 1

        # Check if the current window sums to the target
        if window_sum == target and left <= right:
            res.append(arr[left:right+1])

        right += 1  # Expand the window to the right

    return res
arr = [5,5,10,5,5]
target = 10
subarray_target_sum(arr, target)