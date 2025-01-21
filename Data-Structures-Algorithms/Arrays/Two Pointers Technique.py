#Two Pointer Technique 

##The two-pointer approach is a common technique in algorithm design, 
##especially useful for problems involving arrays or linked lists
##It involves using two pointers (or indices) to traverse the data structure, 
##which can efficiently solve problems related to searching, sorting, or modifying the data

##These pointers can move in the same direction, opposite directions, 
##or can be used for different purposes

# When to Use:

# Searching pairs: In problems where you need to find pairs of elements that meet certain criteria (e.g., sum to a target value).
# Palindromes or Similar Checks: To check if a string or array is a palindrome (same forward and backward).
# Removing Duplicates or Similar Tasks: For example, in a sorted array, removing duplicates or finding unique elements.
# Optimizing Brute Force Solutions: When a naive solution would involve nested loops, two pointers can often reduce complexity.

# Find the Maximum Sum Subarray of a Fixed Size: 
# Given an array of integers and a number k, find the maximum sum of any contiguous subarray of size k

#Keys:
#Contiguos subarrays: Means the elements are adjacent, next to each other, so we need to use a same direction approach

arr = [1,40,2,5,3,4]
k = 3
#Result 44 *[40,2,2]

# Create a variable that store the maximun sum
# loop through the array taking three elements at a time
# compare the sum of these three element to the maximun, if greater then replace it
# move one step to the right

def FindMaximunSum(arr,key):
    maximun_sum = 0
    for i in range(len(arr)-k+1):
        current_sum = sum(arr[i:i+k])
        if current_sum>maximun_sum:
            maximun_sum = current_sum
    return maximun_sum

arr = [1,2,3,6,2,8,4]
k=2
FindMaximunSum(arr,k)

arr = [1, 2, 3, 4, 5]
k = 3

#Fixed Window Approach
def slideWindow(arr,k):
    # Initialize the window sum and maximum sum
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



