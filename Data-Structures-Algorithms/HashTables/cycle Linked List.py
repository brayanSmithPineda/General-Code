class Node:
    def __init__(self,data): 
        self.data = data 
        self.next = None

def cycleLinkedList(head):
    current = head
    hash_map = {}
    while current is not None:
        if current in hash_map:
            return True
        else:
            hash_map[current] = True
            current = current.next
    return False

def floydTortuouseHare(head):
    slow, fast = head
    while fast and fast.next:
        fast = head.next.next
        slow = head.next
        if fast == slow:
            return True 
        
    return False
        