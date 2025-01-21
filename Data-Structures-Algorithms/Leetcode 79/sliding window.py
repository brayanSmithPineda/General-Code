"""
* Given an array of integers, find maximum sum subarray of the required size.
*Input: exmaple = [-1,2,3,1,-3,2]  subarray size: 2
* Out: [1,2] , sum= 5
"""

#Intilize two ponters, this would be our fixed window of size two
#Save the window sum and compare to the max_sum, choose the greater

def maximunSumSubArray(arr, size):

    max_sum = sum(arr[:size-1]) #Initilize the max sum with the first subarray
    start_index = 0 #Intilize the start index at cero

    for i in range(size, len(arr)):
        window_sum = max_sum - arr[i - size] + arr[i]
        if max_sum < window_sum:
            max_sum = window_sum
            start_index = i - size + 1

    return [max_sum, start_index, start_index + size - 1]

my_arr = [-1,2,3,1,-3,2]
size = 2
maximunSumSubArray(my_arr, size)