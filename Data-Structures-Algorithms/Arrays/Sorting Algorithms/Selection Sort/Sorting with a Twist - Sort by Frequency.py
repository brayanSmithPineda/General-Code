"""
Sorting with a Twist - Sort by Frequency

Given an array of integers, sort the array according to the frequency of the elements.If two elements have the same frequency, they should be sorted by their natural order.

arr = [4, 5, 6, 5, 4, 3]
# Sort the array so that elements with lower frequency come first. If frequencies are equal, sort by value.
"""

#As we have to order by frequency we have to track the count each element appears in the array, so we use a hashmap
# after that , we apply the selection sort algorithm ,and this time we compare which count is the lowest so we put it in the min_index

def sory_by_frequency(arr):
    hash_map = {}
    for i in arr:
        if i not in hash_map:
            hash_map[i] = 1
        else:
            hash_map[i] += 1
    
    for left in range(len(arr)):
        minimun_index = left
        for right in range(left, len(arr)):
            if hash_map[arr[right]] < hash_map[arr[minimun_index]]:
                minimun_index = right
            elif hash_map[arr[right]] == hash_map[arr[minimun_index]] and arr[right] < arr[minimun_index]:
                minimun_index = right
        if minimun_index != left:
            arr[minimun_index], arr[left] = arr[left], arr[minimun_index]
    return arr

arr = [4, 5, 6,6,6, 5, 4, 3]
sory_by_frequency(arr)