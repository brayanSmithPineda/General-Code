#The objective here is to traver the array and swapped the elements is the adjacent is grater than the next one, the outer loop determine the number of times we have to traver the array, and the inner loop compare and swapped the elements

#Time complexi O(n**2) and space complexity 0(1)
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Test the function
sample_array = [1,2,3,4,6,5]
bubble_sort(sample_array)
