"""
1. Quick Sort on Linked List
Implement Quick Sort for a singly linked list. The linked list version of Quick Sort is slightly more complex due to the absence of random access. You'll need to modify the partition logic to work on a linked list, which requires extra care with pointer manipulation.
"""
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def quick_sort(arr, left, right):
    if left >= right:
        return arr
    else: 
        # Return the partition index, the pivot index is already in its right position
        pi = partition(arr,left,right)

        quick_sort(arr, left, pi - 1) # Elements smaller than the pi
        quick_sort(arr, pi + 1, right) # Element greater than the pi
        
        return arr

def partition(head,left,right):
    pivot = head.data
    current = head
    i = Node(-1)
    for j in range(left,right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[right] = arr[right], arr[i+1]

    return i + 1
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def get_tail(node):
    while node and node.next:
        node = node.next
    return node

def partition(head, end, new_head, new_end):
    pivot = end
    prev = None
    cur = head
    tail = pivot

    # During partition, both the head and end of the list might change
    # which is why we pass new_head and new_end by reference
    while cur != pivot:
        if cur.value < pivot.value:
            # First node that has a value less than the pivot becomes the new head
            if not new_head:
                new_head[0] = cur
            
            prev = cur
            cur = cur.next
        else:
            # Move cur node to next of tail, and change tail
            if prev:
                prev.next = cur.next
            tmp = cur.next
            cur.next = None
            tail.next = cur
            tail = cur
            cur = tmp
    
    # If pivot data is the smallest element in the current sublist,
    # pivot becomes the head
    if not new_head[0]:
        new_head[0] = pivot

    # Update new_end to the current last node
    new_end[0] = tail

    # Return the pivot node
    return pivot

def quick_sort_recur(head, end):
    if not head or head == end:
        return head

    new_head = [None]
    new_end = [None]

    # Partition the list, new_head and new_end will be updated
    # by the partition function
    pivot = partition(head, end, new_head, new_end)

    # If pivot is the smallest element - no need to recur for the left part.
    if new_head[0] != pivot:
        # Set the node before the pivot node as None
        tmp = new_head[0]
        while tmp.next != pivot:
            tmp = tmp.next
        tmp.next = None

        # Recur for the list before pivot
        new_head[0] = quick_sort_recur(new_head[0], tmp)

        # Change next of last node of the left half to pivot
        tmp = get_tail(new_head[0])
        tmp.next = pivot

    # Recur for the list after the pivot element
    pivot.next = quick_sort_recur(pivot.next, new_end[0])

    return new_head[0]

def quick_sort(head):
    # Get the tail node
    tail = get_tail(head)

    # Call the recursive Quick Sort
    return quick_sort_recur(head, tail)
