"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

#Key here is to notice that if x = target - nums[i] is in our array then we fond the two elements that sum up to the target
#How to we know that x is in our array, we just use a hashmap 
#We intilize an empty hashmap, and we start to adding indixes if x is not in our hashmap, we save the index as the key and element as the value

def twoSumHashTable(nums, target):
    hashmamp = {}
    for i in range(len(nums)):
        x = target - nums[i]
        if x not in hashmamp:
            hashmamp[nums[i]] = i
        else:
            return i, hashmamp[x]
        
    return -1

nums = [2,7,11,15]
target = 26

twoSumHashTable(nums, target)


#another way to do it is to use enumerate() to get the index and the element, that way you do not have to use i and nums[i]

def twosum(array,target):
    hashtable = {}
    for index, element in enumerate(array):
        x = target - element #This is a value of the elements in an array, not an index, this is important because when you do x in hastable(look for x in hashtable) you actually lookin at the key, so the elements should be the key that way when we do x in hashtable our code is going to work
        if x not in hashtable:
            hashtable[element] = index
        else:
            return hashtable[x], index

#the time complexity of this solution is just O(n), we just need to traverse each element at the array just one. the space complexity is also O(n) because in the worst case scenario we do not find any element that sum up to the target and to make sure of that we will need to traverse the entire array and that imply adding the elements to the hashtable