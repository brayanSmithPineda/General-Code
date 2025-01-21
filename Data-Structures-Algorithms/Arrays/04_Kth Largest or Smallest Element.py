# Find the "Kth" Largest or Smallest Element:

# Given an array and a number k, find the kth largest or the kth smallest element in the array.

def findKth (arr,number):
    arr.sort()

    return arr[len(arr)-number]

arr = [1,5,2,3,7,8]
findKth(arr,1)

We can solve this proble with heap sort algorithm, but first we need to understand Binary Tree
dsfsdf
