"""
*Given an array of integers, find maximum sum subarray of the required size.
*Input: exmaple = [-1,2,3,1,-3,2]  subarray size: 2
* Out: elements = [2,3] sum = 5  indixes = [1,2]
"""

#The two pointer we use to traver the array would be the i in the foor loop and the size variable we are given as input
#Traverse the array with a window of size two, in each iteration when you calculate the window_sum substract the i - k value and add the i value

def maximun_sum_subarray(arr, size):
    maximun_sum = sum(arr[:size])
    window_sum = maximun_sum
    start_index = 0
    for i in range(size, len(arr)):
        window_sum = window_sum + arr[i] - arr[i - size]
        if window_sum > maximun_sum:
            maximun_sum = window_sum
            start_index = i - size + 1
    return [maximun_sum, start_index, start_index + size - 1]

arr = [1,2,3,0,1,6]
size = 2
maximun_sum_subarray(arr, size)

def maximun_sum(arr, size):
    if len(arr) < size:
        return "Array is too short"

    maximun_sum = sum(arr[:size])
    window_sum = maximun_sum
    start_index = 0

    right = size #Element to be added
    left = right - size  #Element to be substracted

    while right < len(arr):
        window_sum = window_sum + arr[right] - arr[left]

        if window_sum > maximun_sum:
            maximun_sum = window_sum
            start_index = left + 1

        right += 1
        left += 1
    return [maximun_sum, arr[start_index:start_index+size] [start_index, start_index + size - 1]]
arr = [1,2,3,0,1,6]
size = 2
maximun_sum(arr, size)