
class Arrays:
    def __init__(self):
        self.data = [] #Intialize an empty array

    def addElementEnd(self, element):
        self.data.append(element)

    def addElementAtAnyPosition(self, index, element):
        self.data.insert(index, element)

    def removeElementbyValue(self, element):
        self.data.remove(element)

    def removeElementByIndex(self, index):
        self.data.pop(index)

    def displayArray(self):
        print(self.data)

    def getByIndex(self, index):
        if 0 <= index <  len(self.data):
            return self.data[index]
        else:
            return 'index out of bound'

class Arrays:
    def __init__(self):
        self.data = []
        self.count = 0
    def append(self, element):
        """Insert at the end of the list"""
        if len(self.data) == self.count:
            self.data += [None]
        else:
            self.data[self.count] = [element]
            self.count += 1
    def appendAtBeginning(self,element):
        if len(self.data) == self.count:
            self.data += [None]
   
        for i in range(len(self.data), 0, -1):
            self.data[i] = self.data[i -1] #Shift all elements to the right
        self.data[0] == element
        self.count += 1

    def appendAtAnyIndex(self,element, index):
        if len(self.data) == self.count:
            self.data += [None]
        for i in range(len(self.data), index, -1):
            self.data[i] == self.data[i-1] #Move elements to the right
   
        self.data[index] == element
        self.count += 1

    def deleteAtEnd(self):
        if self.count == 0:
            return 'Array is empty'
        
        self.data[self.size - 1] == 'None'

        self.count -= 1
    
    def deletAtBeginning(self):
        if self.count == 0:
            return 'Array is empty'
        
        for i in range(1, len(self.data)):
            self.data[i - 1] == self.data[i] #Shif the element to the left
        self.data[len(self.data) - 1] = None #Clear the last duplicated element
        self.count -= 1 #Updated the size
    
    def deleteAtAnyIndex(self, index):
        if self.count == 0:
            return 'Array is empty'
        
        for i in range(index,len(self.data)):
            self.data[i] = self.data[i + 1]
        
        self.data[len(self.data) - 1] = None
        self.count -= 1

class HashTable:
    def __init__(self):
        self.data = {}
    
    #Insert a key value-pair
    def add(self, key, value):
        self.data[key] = value 
    
    #Remove a key-value pair by its key
    def removeByKey(self,key):
        if key in self.data:
            self.data.pop(key)
        else:
            return 'Key is not in the hashmap'
        
    #Display content of the hashtable
    def display(self):
        for key, value in self.data.items():
            return [key, value]

    #Get a the value by its key
    def getValue(self, key):
        """Retrieve the value associated with a given key in the hashtable."""
        return self.data.get(key, None)    
    
    #Get the key by its value
    def getKey(self, val):
        for index, value in self.data.items():
            if value == value:
                return index
        return None

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def preappend(self, data):
        """Append a node to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def append(self, data):
        """Append a node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while  current.next is not None:
                current = current.next
            current.next = new_node

    def appendAtSpacificNodeValue(self, data, targetData):
       """Insertion: After a specific Node""" 
       new_node = Node(data)
       current = self.head
       while current.next is not None:
            if current.data == targetData:
                new_node.next = current.next
                current.next = new_node
                return #This return statement is to exit the loop there is no reason to continue
            current = current.next

    def delete_firt_node(self):
        if not self.head:
            return 'Linked-list already empty'
        else:
            self.head = self.head.next

    def delete_last_node(self):
        if not self.head or not self.head.next: #If the list is empty or has one element set the head to point to None
            self.head = None
            return

        current = self.head

        while current.next.next:
            current = current.next

        current.next = None

    def deleteFirstOccurrence(self, data):
        """Delete the first occurrence of a node by value."""
        if not self.head:
            return 'Linked list is empty'
        if self.head.data == data:
            self.head = self.head.next
            return self.head

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                break
            current = current.next

    def deleteAllOccurrence(self, data):
            """Delete All occurrence of a node by value."""
            while self.head and self.head.data == data:
                self.head = self.head.next

            current = self.head
            while current and current.next:
                if current.next.data == data:
                    current.next = current.next.next
                else:
                    current = current.next
            return self.head

    def deleteAllOccurrencesDummyNode(self, data):
        dummy = Node(-1)
        dummy.next = self.head
        previous = dummy
        current = self.head
        while current:
            if current.data == data:
                previous.next = current.next
                current = current.next
            else:
                previous = current
                current = current.next
        return dummy.next

    def searchByValue(self, data):
        """Search for a node by value. Returns True if found, False otherwise."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    def display(self):
        """Prints the contents of the linked list."""
        current = self.head
        while current:
            print(current.data, end = '->')
            current = current.next
        print('None')

    def seachByValue(self, value):
        """Search for a node by value. Returns True if found, False otherwise."""
        current = self.head
        while current.next:
            if current.data == value:
                return True
            else:
                current = current.next
        return False
    
class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, element):
        """Add element to the stack(we just can insert at the end)"""
        self.data.append(element)

    def pop(self, element):
        """Remove an element from the stack(we just can remove from the end)"""
        if len(self.data) == 0:
            return "Stack is empty"
        
        self.data.pop()

    def peek(self):
        """Return the last element of the stack"""
        if len(self.data) == 0:
            return 'Array is empty'

        return self.data[-1]
    
    def isEmpty(self):
        return len(self.data) == 0
    
    def size(self):
        return len(self.data)

class Stacks:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data += [element]
    
    def pull(self):
        if len(self.data) == 0:
            return 'Array is empty'
        
        element_pop = self.data[-1]
        
        self.data = self.data[:-1]
        return element_pop, self.data

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        #You can only add at the end
        self.items.append(data)
        return self.items
    
    def dequeue(self):
        #You can only remove the first element
        if not self.items:
            self.items.pop(0)
            return self.items
        return 'Queue is empty'
    
    def peek(self):
        #Return the element at the front(first) of the queue
        if not self.items:
            return self.items[0]
        return 'Array is empty'
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, element):
        self.items += [element]

    def dequeue(self):
        if len(self.items) == 0:
            return 'It is empty'

        pop_element = self.items[0] 
        for i in range(1,len(self.items)):
            self.items[i-1] = self.items[i]

         # Remove the last element since it's now a duplicate after shifting.
        self.items = self.items[:-1]    

        return pop_element, self.items   
    
class Tuple:
    """Data Structure that store order collections of elements, It can contain duplicate elements. The elements are immutable, can not be change it """
    def __init__(self, initial_elements = None):
        self.tuple = tuple(initial_elements) if initial_elements else ()

    def add(self, element):
        """As tuples are immutable we can not add, remove or change its content. so to add a element we need to create a new tuple, that new tuple would be the concatenation the initial tuple with the element you want to insert"""
        self.tuple = self.tuple + (element,)
    
    def remove(self, element):
        new_tuple = ()
        for i in self.tuple:
            if i != element:
                new_tuple = new_tuple + (element,)

        self.tuple = new_tuple #we assign new_tuple back to self.tuple.

    def getElement(self, index):
        return self.tuple[index]
    
    def display(self):
        print(self.tuple)

class Sets:
    """
    1- Sets are mutable, means that we can add, remove or change its content
    2- Sets are unorder, means the we can not access the element by its index
    3- Sets stores unique elements, we can not have duplicates
    """
    def __init__(self, initial_elements):
        self.set = set(initial_elements) if initial_elements else set()

    def add(self, element):
        self.set.add(element)
    
    def remove(self, element):
        if element in self.set:
            self.set.remove(element)
        else:
            return 'Element not in set'
        
    def getItem(self,element):
        if element in self.set:
            return element

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, source_node, destination_node):
        if source_node in self.graph and destination_node in self.graph:
            self.graph[source_node].append(destination_node)
            # self.graph[destination_node].append(source_node) undirected graph
    
    def print_graph(self):
        for node in self.graph:
            print(f"{node}-->{self.graph[node]}")
    
class Tree:
    def __init__(self, root):
        self.root = root
        self.childrens = []
    
    def traverse_BFS_printTree_eachLevel(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            current_nodes_level = []
            current_level_size = len(queue)
            for _ in range(current_level_size):
                node = queue.pop(0)
                current_nodes_level.append(node.data)

                for child in node.childrens:
                    queue.append(child)
            res.append(current_nodes_level)
        return res
            
    def print_only_nodes_without_following_any_level(self, root):
        if not root:
            return
        print(root.data)
        for child in root.childrens:
            self.print_only_nodes_without_following_any_level(child)
        


