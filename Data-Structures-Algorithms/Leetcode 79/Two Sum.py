#Two Sum
#Given an array of integers, return Indices of the two numbers such that they add up to a spefic target 

#You may assume that each input would have exactly one solution, and you may not use the same element twice

# arr = [2,11,7,15] target = 9
# outpu: [0,1]

# Array data strcuture
# Hashmap
# Key - Notice that the value we are looking for is the difference bewteen the target and the current number if we traverse the array target -i = value, if we are at two then we can say if 9 - 2 = 7 exist in our array then we found the two indices, so here as we want to see if a number is in an array we can do this i O(1) with hasmap

#How to we add the elements to the hashmap to check is the number is in the array?
# ---- 1 - we declere an empty hashmap
# ---- 2 - we traverse the array and check if target - current is in the hasmap (at first when the hashmap is empty is going to always be false)
# ---- 3 - if target - current is not in the hashmap we add it, and then continue the loop  
# ---- Note: The key here is that sum is associat, so if we fist find 2 and we're looking for the 7 and we did not find it in the hashmap, is ok because then when we are at the position of the element value 7 we are goin to find the 2 element, is the same to say 2 + 7 that 7 + 2

def twoSum(arr, target):
    hash_map = {} # Store the elements as keys, and the indexes as values
    for index, element in enumerate(arr):
        complement = target - element
        if complement in hash_map:
            return index, hash_map[complement]
        else:
            hash_map[element] == index
    return 'Not Found'

arr = [1,3,3,6]

for i, j in enumerate(arr):
    print(i,j)