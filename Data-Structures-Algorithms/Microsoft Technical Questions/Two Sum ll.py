"""
167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space. #This means we can use a hashmap again as we did you two sum l

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
"""

#The key here is to notice that the array is sorted, so with that we can use two pointer techinique to divide the search array by half.

#Initilize two pointer, at the start and at the end
#we sum those two indices and compare it with the target, if its equal we just return the indeces, if the sum is less than the target we know that we have to move the left pointer to the right, else we move the right pointer to the left

def sumSorted(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left+1,right+1]
        elif current_sum < target:
            left += 1
        else: 
            right -= 1

numbers = [2,7,11,15]
target = 9

sumSorted(numbers, target)