#Fixed Window Approach
def slideWindow(arr,k):
    #maximum sum
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum

#Dynamic Window Approach
# Minimum Size Subarray Sum: 
# Given an array of positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
# Input:
# Array: [2, 3, 1, 2, 4, 3]
# Positive Integer s: 7
# Output:
# Minimal Length of Contiguous Subarray: 2

#Left and right pointers to track our window
# so if our window sum (total variable) is less than the integer then we are going to increment our window by moving our right pointer one step to the right and continue doing until the sum >= s
#when sum>= s we are going to save the lenth
# After we save the length we decrement the left point by one and continue doing the steps before
def minSubArrayLen(s, nums):
    n = len(nums) 
    min_length = float('inf') #Lenght of the minimun subarray
    current_sum = 0 #Just initialize the current sum, total
    left = 0 #Just initialize Left point

    for right in range(n):
        current_sum += nums[right] # Update the sum everytime we increase the window

        while current_sum >= s:
            min_length = min(min_length, right - left + 1) #minumum length
            current_sum -= nums[left] # get rid of the left element in the sum
            left += 1 # get rid of the left element in the window

    return 0 if min_length == float('inf') else min_length #Return 0 in case we do not find the min length

