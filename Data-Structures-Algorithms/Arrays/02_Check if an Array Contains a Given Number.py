#2- Check if an Array Contains a Given Number:

## Implement a function to check if a certain number is present in an array.

# Algorithm
# 1- loop the array
# 2- check if i is equal to the target
# 2- return true + i + number

def checkNumber(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f"fin the number {arr[i]} at position {i}"
    return "Not Found"

arr = [12,3,4,5,6]

checkNumber(arr,1)