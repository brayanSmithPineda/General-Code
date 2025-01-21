"""
1051. Height Checker

The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].

Example 1:

Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.
"""

def heigh_checker(arr):
    temp = arr[:]
    for i in range(len(arr)-1):
        swaped = False
        for j in range(len(arr)-1 -i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaped = True
        if swaped == False:
            break
    count = 0
    for i in range(len(arr)):
        if temp[i] != arr[i]:
            count+=1

    return count

heights = [1,1,4,2,1,3]
temp = heights
temp
heigh_checker(heights)

def heigh_checker2(arr):
    count = 0
    sorted_array = sorted(arr)
    for i in range(len(arr)):
        if arr[i] != sorted_array[i]:
            count += 1
    return count