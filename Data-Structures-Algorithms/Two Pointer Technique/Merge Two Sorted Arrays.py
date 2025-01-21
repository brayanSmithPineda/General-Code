# Merge Two Sorted Arrays:
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array. The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

# Example:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: nums1 = [1,2,2,3,5,6].

#First to merge and array we could use bracket notion nums[len(arr)-1] = nums[1] for example.
# The key here is to compare each element of the two arrays and put it in the positions starting from the right(greater value)
#so we should go like this, if nums2[n] > nums1[m], we now that the non zero element of nums of 1 are m and the len of nums 2 is n, if the condition is met we sould put the element of nums 2 in the last position of the array, so here we also need a pointer that decrement the last position, we do not want to update always the las position we need to go through the array

#Create a variable that store the las position, initilize it with len(arr)-1
#create two pointers, one to get the last revised element of nums1(m) and the other for nums2(n)
#loop through the arr until m >=0 and n >=0, that means there is no more numbers to analyze
# if nums1[m]  > nums2[n], we need to put nums1[m] in the last position, then decrement the last variable
# if nums1[m]  =< nums2[n], we need to put nums1[n] in the last position, then decrement the last variable

def mergeTwoSortedArrays(arr1,arr2,m,n):
    last = m + n - 1 # the same as len(arr1) -1
    while m > 0 and n > 0:
        if arr1[m-1] > arr2[n-1]:
            arr1[last] = arr1[m-1]
            m -= 1
        else: 
            arr1[last] = arr2[n-1]
            n -= 1 
        last -=1
    
    while n>0:
        arr1[last] = nums2[n-1]
        n, last = n-1, last-1
    return arr1
nums1 = [2,2,3,0,0,0]
m = 3
nums2 = [1,5,6]
n = 3

mergeTwoSortedArrays(nums1,nums2,m,n)
# Output: nums1 = [1,2,2,3,5,6].