def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

def merge(left, right):
    left_index, right_index = 0, 0
    result = []

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    if left:
        result += left[left_index:]
    if right:
        result += right[right_index:]

    return result
# Test the function
sample_array = [38, 27, 43, 3, 9, 82, 10]
merge_sort(sample_array)

