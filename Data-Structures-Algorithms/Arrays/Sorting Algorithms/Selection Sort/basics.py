def selection_sort(arr):
    for left in range(len(arr)):
        min_index = left
        for right in range(left+1,len(arr)):
            if arr[right] < arr[min_index]:
                min_index = right
                
        arr[left], arr[min_index] = arr[min_index] , arr[left]
    return arr

sample_array = [64, 25, 12, 22, 11]
selection_sort(sample_array)