#With this approach, we sort the algorithm using extra space to save the left section(elements less or equal to the pivot) and right section(elements greater than the pivot)
def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        left_sort = [x for x in arr[:-1] if x <= pivot]
        right_sort = [x for x in arr[:-1] if x > pivot]
        return quick_sort(left_sort) + [pivot] + quick_sort(right_sort)
    
sample_array = [3, 6, 8, 10, 1, 2, 1]
quick_sort(sample_array)

#In- Place sort approach

def quickSort(arr, left, right):
    if left < right: #if this condtion is not met that means we have a single arra element, there is no need to sort it
        #pi is partition index, now arr[pi] is in the right place
        pi = partition(arr,left, right)

        #Separately sort the elements before and after partition
        quickSort(arr, left, pi -1)
        quickSort(arr, pi + 1, right)
    return arr

def partition(arr, left, right):
    pivot = arr[right]

    i = left - 1
    for j in range(left,right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[right] = arr[right], arr[i+1]

    return i + 1

sample_array = [3, 6, 8, 10, 1, 2, 1]
quickSort(sample_array, 0, len(sample_array)-1)