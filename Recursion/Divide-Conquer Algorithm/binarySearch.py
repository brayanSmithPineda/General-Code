#Binary search recursive way
def binarySearch(arr, left, right, target):
    if left > right:
        return -1
    else:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            return binarySearch(arr, mid + 1, right, target)
            
        else:
            return binarySearch(arr, left, mid - 1, target)

arr = [2, 3, 4, 10, 40]
target = 10

binarySearch(arr, 0, len(arr) - 1, target)