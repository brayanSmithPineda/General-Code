# 169. Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3

#Create an emty hash map to store the as keys the elements in nums, and the values to be the number of time each element appears at nums
#Compare if len(arr)/ 2 > count if its then return the element, if not then sum 1 to the count

def majorityElement(arr):
    hash_map = {}
    majorityElement = len(arr)/2
    for i in range(len(arr)):
        if arr[i] not in hash_map:
            hash_map[arr[i]] = 1

        else:
            hash_map[arr[i]] += 1 

        if hash_map[arr[i]]> majorityElement:
            return arr[i]
        
nums = [3,2,3]
majorityElement(nums)

#Key:
#1-- if we need to count the number of ocurrences in a hastable, we just have to initialize the value with a one, and then increase with has_map[key] += 1 to increment the count

#2- we can use multiple if statement to check multiple contiones, each element is going to be evaluated in each condition, in this example we check if the current number is in i and its count is greater than the Majority Element, for that we need to use if instead of elif, beacause are two different conditions, elif are exclusive so if we write elif is not going to check if already meets a previos condtion