#This is the class of arrays
class Arrays:
    def __init__(self):
        self.data = [] #Intialize an empty array

    def addElementEnd(self, element):
        self.data.append(element)

    def addElementAtAnyPosition(self, index, ele    ):
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





# The most common representation of an array in python are lists

my_arr = [1,2,3,4]

#Types of Arrays Operations
#1-Travelsal : travers through the elements of an array
#---- Travelsal is the process of going through the array elements one by one
#----To traverse an array in Python, you use a loop.
for i in my_arr:
    print(i)    

#--- There are three important reasons for travelsal
    #-- Inspecting elements : look for something
     #Example: Finding Negative Numbers in an Array
        #Suppose you have an array of numbers and you want to check if there are any negative numbers in it.
numbers = [1,-2,3,-4]


def numberOfNegativeNumbers(numbers):
    count = 0
    for i in numbers:   
        if i<0:
            count+=1
    return count

numberOfNegativeNumbers(numbers)

#-- Performing operations in each element
     #Example: Doubling the Values in an Array
        #Consider an array where you want to double the value of each element.
arr = [1,2,3,4]
for i in range(len(arr)):
    arr[i] *=2

print(arr)

new_arr = []
for i in arr:
    new_arr.append(i*2)
print(new_arr)

#-- Collecting Information from the Array
     #Example: Summing All the Elements in an Array
        #If you have an array of numbers and want to find the total sum of these numbers, you can do so using traversal.

my_list = [1,2,3]
my_sum = 0
for i in my_list:
    my_sum +=i

my_sum

#Types of Arrays Operations
#1-Insertion : Insertion refers to the process of adding a new element to an array (list in Python) at a specific position.
#---- Insertion with append() built-in python method, add element at the end. O(1)
array_1 = [1,2,3,4]
array_1.append(5)
array_1
#---- Insertion with intert() built-in python method, add element at any position. O(n), it require shifting each of the existing elemnts to the right
array_2 = [1,2,3,4]
array_2.insert(2,5)
array_2
##---- Insertion with slicing, not built in methods. O(n) complexity, slice imply to create a new list by copying the element,concatenation is also o(n)
array_3 = [1,2,3,4]
new_number = 5
position = 1
array_3 = array_3[:position]+[new_number]+array_3[position:]
array_3

##----Use Cases: a. Maintaining Sorted Order:
# ----Suppose you have a sorted list of numbers and you want to insert a new number while maintaining the sorted order.
numbers2 = [1, 3, 4, 7, 8]

new_number = 5

for i in range(len(numbers2)):
    if numbers2[i] > new_number:
        numbers2.insert(i,new_number)
        break
else:
    numbers2.append(new_number) 
numbers2

#Types of Arrays Operations
#1-Deletion : Deleting element from the array.
#---- Deletion with del statement:it removes the specified element(s) from the list.

example = [1,2,3,4]
del example[2]
example

#---- Deletion with remove method:it removes the first occurrence of a specified value from the list.

example = [1,2,3,4]
example.remove(4)
example

#---- Deletion with pop method:it removes and returns the element at a given index.

example = [1,2,3,4]
example.pop(0)
example

#--- Note: all deletion methods requires shifting all the elements to the right of the delete element to the left so it require O(n)

#Types of Arrays Operations
#1-Searching : where you look for the presence of an element within the array.It involves checking each element of the array until you find the desired one or conclude that it's not present

#Linear Searh Algorithm (Sequencial Search)
#---It checks every element of the array one by one. O(n)
# #Here is the algorithm
# ---1.Start at the beginning: Begin at the first element of the list.
# ---2.Check each element in turn: Compare the current element with the element you're searching for.
# ---3.If a match is found: Return the index of the element or indicate that the element is found.
# ---4.If the end of the list is reached: If you reach the end of the list without finding the element, conclude that the element is not present in the list.

def linearSearch(array, serchingElment):
    for i in range(len(array)):
        if array[i] == serchingElment:
            found = True
            return i, array[i]           
    return 'Not found'
    
test = [1,2,3,4]

element = 5

linearSearch(test,element)

#Binary Search Algorithm (Sequencial Search)
#---Binary Search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one. O(logn)
# #Here is the algorithm
# ---1.Compare the middle element: Check if the middle element of the array is equal to the target element
# ---2.Left or Right: If the target element is smaller, narrow the search to the left half of the array, otherwise to the right half.
# ---3.Repeat: Continue the process on the new half-array until the element is found or the subarray size becomes zero.
# Initial Setup: Start with two pointers, typically called low and high, at the beginning and end of the array respectively.

# Find the Middle: In each step, look at the middle element of the array (or sub-array). The middle element is found by mid = low + (high - low) // 2.

# Compare with the Target:

# If the middle element is equal to the target, you've found the item.
# If it's less than the target, adjust the low pointer to mid + 1.
# If it's greater than the target, adjust the high pointer to mid - 1.
# Repeat or Conclude: Repeat these steps until the low pointer exceeds the high pointer, which means the element isn't in the array.

def binarySearch(array,searchingValue):
    low, high = 0, len(array)-1
    
    while low<=high:
        middle = low+ (high-low)//2
        if array[middle] == searchingValue:
            return array[middle], middle
        elif array[middle] < searchingValue:
            low = middle + 1
        elif array[middle] > searchingValue:
            high = middle - 1
    return -1

test2 = [1,2,3,4,5]
binarySearch(test2,5)

#Types of Arrays Operations
#1-Sorting: Maintaining the order of elements in the array.

##Bult-in methods for sorting, sorted() and sort()

#---Sorted (): in this case the sorted method creates a new list

arr = [1,2,5,2,4,6]
new_arr = sorted(arr, current=None, reverse=False)
new_arr
arr = ['b','sm','pin','duar']
new_arr = sorted(arr,current=len, reverse=True)
new_arr

#---Sort(): Sorts the list in place (modifies the original list).

arr = [1,2,5,2,4,6]
arr[0], arr[1] =arr[1] , arr[0]
arr
arr.sort(current=None, reverse=False)
arr

#-- Sorting Algorithms
##---Bubble sort

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            print('it is already order')
            break

#Time Complexity: O(n²) in the worst and average cases. O(n) in the best case if the list is already sorted.
        

arr = [1,2,3,4,5]
bubbleSort(arr)
arr

##-- Selection sorting 
# Start with the first element of the array as the minimum.
# Compare this minimum with the rest of the array.
# If a smaller element is found, consider it the new minimum and continue until the end of the array.
# After completing the first pass, swap the minimum found with the first element of the array.
# Move the boundary of the unsorted subarray by one element to the right.
# Repeat the above steps until the array is sorted.

#--- Time complexity : o(n^2)
def selectionSorting(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[min_index], arr[i] = arr[i], arr[min_index]

arr = [1,5,6,2,0,2,8,7,9,3]
selectionSorting(arr)
arr

# Insertion Algorithm
## 1-- Take the second element as the current element
## 2-- Compare the current element with the elements at the sorted part (left part)
## 3-- if current element is less than the element at the left make an space (copy the left element to the right)
## 4-- put the current element at the empty spot

def insertionSorting(arr):
    n = len(arr)
    for i in range(1,n):
        current = arr[i]
        j = i - 1
        while j >= 0 and current < arr[j]:
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = current

arr = [3, 4, 5, 8, 2]
insertionSorting(arr)
arr


# Two Pointer Approach
# Understanding Two-Pointer Approach:
# What It Is: It involves two references (pointers or indices) that move through an array (or linked list) to solve a problem. These pointers can move in the same direction, opposite directions, or can be used for different purposes.

# 1. Opposite Direction Pattern
# Scenario: Finding a pair with a specific sum in a sorted array.
def sumProblem(arr, target):
    left, right = 0, len(arr)-1
    while left<right:
        current_sum = arr[left]+arr[right]
        if current_sum == target:
            return 1
        elif current_sum < target:
            right -= 1
        elif current_sum > target:
            left +=1


    return -1

arr=[1,2,3,4,5]
target = 6

sumProblem(arr, target)

# 2. Same Direction Pattern
# Scenario: Removing duplicates from a sorted array.

def removeDuplicates(arr):
    if not arr:
        return 0
    unique = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[unique]:
            unique += 1
            arr[unique] = arr[i]
    return unique + 1, arr[:unique+1]  # Length of array without duplicates
