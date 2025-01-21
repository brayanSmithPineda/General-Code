def insertion_sort(arr):
    for i in range(1,len(arr)):
        current = arr[i]

        left = i - 1
        while left >= 0 and arr[left] > current:
            arr[left+1] = arr[left]
            left -= 1
        
        arr[left+1] = current
    return arr

arr= [4,5,3,2,1]
insertion_sort(arr)