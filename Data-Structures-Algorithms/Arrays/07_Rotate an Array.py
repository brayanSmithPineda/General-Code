# Rotate an Array:

# Write a function that rotates an array to the right by a given number of steps.

# Input:

# Array: [1, 2, 3, 4, 5, 6, 7]
# Number of steps to rotate: 3
# Expected Output:

# The array after rotating 3 steps to the right: [5, 6, 7, 1, 2, 3, 4]

#concatenate arr[:steps:-1] + arr[steps+1:]

def rotateArray(arr,steps):
    return arr[:steps:-1] + arr[:len(arr)-steps]

arr = [1, 2, 3, 4, 5, 6, 7]
steps = 3
rotateArray(arr,steps)

def rotateArray(arr,steps):
    res = [None]*len(arr)
    for i in range(len(arr)):
        position = (i + steps) % len(arr)
        res[position] = arr[i]
    return res
arr = [1, 2, 3, 4, 5, 6, 7]
steps = 3
rotateArray(arr,steps)
