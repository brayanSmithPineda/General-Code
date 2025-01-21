# 1- Find the Maximum and Minimum Element in an Array:

### Write a function to find the maximum and the minimum element in an array.

#Algorithm
# 1- Create two variable, max and min that store the maximum value and minimun value of the array
# 2- loop through the array and compare each element with the max and min
# 3- if the max < i then replace max with i, and if min>i then replace min with i
# 4- retunr max and min 

i
import math

def findMaxMin(arr):
    max = arr[0]
    min = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
    return max, min
arr = [2,2]
findMaxMin(arr)