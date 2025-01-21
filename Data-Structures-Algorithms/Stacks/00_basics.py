class Stack:
    
    #Intilizize a stack
    def __init__(self, length):
        self.stack = [None]*length #Initilize a stack with a fixed size
        self.last = -1 #We initilize a variable pointing to the last position of the stack,in this case as is empty is initialize at -1

    #Add an element to the stack (add to last position)
        
    def addElement(self, element):
        if self.last < len(self.stack) - 1: #Checks for stack overflow (out of bound)
            self.stack += 1
            self.stack[self.last] = element
        else:
            return "Is full"
        
    #Remove an element from the stack (remove from last element)
        
    def removeElement(self):
        if self.last >= 0: #Check if Stack is not empty
            remove_element = self.stack[self.last]
            self.last -= 1
            return remove_element
        return "Is Empty"

    # Peek: Returns the top item from the stack without removing it.
    
    def peek(self):
        if self.item >= 0:
            return self.stack[self.item]
        else:
            return "Is Empty"
        
    # IsEmpty: Checks if the stack is empty.
        
    def isEmpty(self):
        if self.last >= 0:
            return "Is not empty"
        return "Is empty"
    
    # Size: Returns the number of items in the stack.

    def size(self):
        return self.top + 1

