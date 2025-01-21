"""
Merge Sort with Inversion Count
    
Enhance the Merge Sort algorithm to count the number of inversions in the array. An inversion is a pair of elements (a[i], a[j]) such that i < j and a[i] > a[j]. This problem will help you understand how to extend the Merge Sort algorithm to compute additional information during the merge step.

Input: [8, 4, 2, 1]
Output: Number of inversions = 6
(The pairs are (8,4), (8,2), (8,1), (4,2), (4,1), and (2,1))
"""
arr = [1]
sum(range(len(arr)))

#First we sort the input with merge sort and then we return the number of inversions

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        mid = len(arr) // 2
        left, left_inversions = merge_sort(arr[:mid])
        right, right_inversions = merge_sort(arr[mid:])
        
        merged, merged_inversions = merge(left, right)

        total_inversions = left_inversions + right_inversions + merged_inversions

        return merged, total_inversions 

def merge(left,right):
    result = []
    left_index, right_index = 0, 0
    inversions = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
            inversions += len(left) - left_index
    
    if left:
        result += left[left_index:]
    if right:
        result += right[right_index:]

    return result, inversions

arr = [8, 4, 2, 1]
merge_sort(arr)