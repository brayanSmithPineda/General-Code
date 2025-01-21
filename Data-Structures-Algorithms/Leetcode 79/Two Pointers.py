# 121. Best Time to Buy and Sell a Stock

# Say you have an array of which the ith element if the price of a given stock on a day i.

# if you were only permitted to complete at most one transaction (i.e buy one and sell one share of the stock), design an algorithm to find the maximun profit

# Note you can not sell a stock before you buy one

# Example1
# input [7,1,5,3,6, 4]
# output: 5
# Explanation: Buy on day 2 (price 1) and sell on day 5 (price 6), profit = 6-1 = 5 


#The key here is that we are looking for the lowest buy price (first element we need to choose), and the highest sell price

#So with this in mind, how to we do to find the lowest and maximun elements, well the key is the profit.

#We are going to have to pointer, left and right, the left is going to be pointed at the buy price and the right one at the sell price. so if we do right - left we find the profit, so we need to continue move this pointer through the array until we find max profit. 

#How do we now is the two pointers technique, always think that this algorithm look for a conjuntion operations within two elements, for example the pair of elements that add up to the maximun number.

# Define the left and right pointers at 0 at 1, define a variable that store the max_profit
# Traver the array with the right pointer, if left < right, that means we found a lower buy price so we shift left = right
# in any case with shift right one step to the right, and we calculate the current_profit = rigt - left
# we campare the current_profit with the max_profit and we choose the maximun

def buySellStock(arr):
    left = 0
    max_profit = 0
    for right in range(1,len(arr)):
        current_profit = arr[right] - arr[left]
        if arr[left] > arr[right]:
            left = right
        max_profit = max(max_profit, current_profit)

    return max_profit

# ###More Two- Pointers Problems
# 26. Remove Duplicates from Sorted Array

# Given an interger array nums sorted in ascending order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same. then return the number of unique elements in nums

# 1- Change the array nums, such that the first k elements of nums contains the unique elements in order they were presented in nums initially. the remaining elements of nums are not important as well as the size of the array.
# 2- return k, number of unique elements (length)

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores)

#The key here is to overwrite the element that is a duplicate
# So here we need to move the elements to the right when the have a unique element
# the left pointer is going to track the position where we need to overwrite or replace the value, in this case is going to be at the postion that is not unique
# the right pointer is going to traverse the array
# so we initilize the left and right at 1 (the first position is going to always be the same), if right != right -1 then that means is a unique element so we updated left and right one step to the right, else that means they are duplicates element so we updated right and leave left pointing a that duplicate element
# if right != right -1 we move the the element at the right position wherever the left position is pointing at

def removeDuplicates(arr):
    left, right = 1, 1
    while left < len(arr) and right < len(arr):
        if arr[right] != arr[right - 1]:
            arr[left] = arr[right]
            left += 1
        right += 1
    return left, arr[:left]


# #Remove Elements
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores)

#The left pointer is going to track the ocurrences of the val element, and the right is going to traver the array
#every time left == val, we overwrite the value with the next one

def removeElement(arr, val):
    left, right = 0, 0
    while left < len(arr) and right < len(arr):
        if arr[right] != val:
            arr[left] = arr[right]
            left += 1
        right += 1
    return left

# Two sum ll input array sorted
#Given a 1-indexed array of intengers that is already sorted in ascending order, find the two numbers such that they add up to the target. Return the indicies of the two numbers

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

#KEY: The array is sorted, the need to find a pair of elements that meet certain criteria (sum = target), in this case we were given a target number (not as the stock that we were not) so the key is to compare the current sum of the two pointers with the target, if current_sum < target that means we need to move the left pointer, else the right pointer

def twSumSortedArray(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    

# 977. Squares of a Sorted Array  
# Given an integer array sorted in ascending order, return an array of the squares of each number sorted in ascending order 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
            
#The key here is to build the  sorted squeare array in reverse order, so we intilize to pointer, one at the end and one the start, and we compare the square of each and decide which one is the maximun, then we insert that maximun in the las position of the array

def squaresSortedArray(arr):
    left, right = 0, len(arr)-1
    new_arr = [None]*len(arr)
    last = len(new_arr) -1
    while left <= right:
        if (arr[left])**2 <= (arr[right])**2:
            new_arr[last] = (arr[right])**2
            right -= 1
            last -=1
        else:
            new_arr[last] = (arr[left])**2
            left += 1
            last -=1
    return new_arr

# Backspace String Compare:
# Given two strings S and T, return true if they are equal when both are typed into empty text editors. # means a backspace character. Use two pointers to compare the strings from the end, considering the backspace characters.

# Example: S = "ab#c", T = "ad#c"
# Solution: true (Both strings become "ac") 

#Key, here we need to create a helper funtion to handle the valid characters that we need to compare, so we first define a function to do that (return the indeces of the character we need to compare) and then with a while loop we compare the valid characters, all the operations are perform right to left becase that's the direction the # remove elements

def backspaceCompare(S, T):
    i, j = len(S) -1, len(T) - 1
    def nextValidCharacter(index, string):
        number_of_backspaces = 0
        while index >=0:
            if string[index] == '#':
                number_of_backspaces += 1
            elif string[index] != '#' and number_of_backspaces >0:
                number_of_backspaces -= 1
            elif string[index] != '#' and number_of_backspaces == 0:
                return index
            index -= 1
        return index
    
    while i >= 0 or j >= 0:
        i = nextValidCharacter(i, S)
        j = nextValidCharacter(j, T)
        if i >= 0 and j>=0 and S[i] != T[j]:
            return False
        if (i >= 0) != (j >= 0):
            return False
        i -= 1
        j -= 1
    return True

S = "bbbextm"
T = "bbb#extm"

backspaceCompare(S,T)

#This problem can also be solved by the stack algorithm, the key here is to start addind element to the stack if the character is not #, if the character is equal to # then remove the last element from the stack

def backspaceStack(s,t):
    def buildStack(string):
        stack = [None]*len(string)
        last = -1
        index = 0
        while index <= len(string) - 1:
            if string[index] != '#':
                last += 1
                stack[last] = string[index]
            else:
                if last >=0:
                    stack[last] = None #Optional
                    last -= 1
            index += 1
        return stack[:last+1]
    return buildStack(s) == buildStack(t)

S = "ab#c"
T = "ad#c"
backspaceStack(S,T)

#Merge Sorted Arrays
#Given two sorted integer arrays 'nums1' and 'nums2', merge 'nums2' into 'nums1' as one sorted array.The number of elements intilized in 'nums1' and nums2 are m and n respectively. You may assume that nums1 has enough space (size that is equal to m+n) to hold addtional elements from nums2. 

# Example: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Solution: After merging, nums1 = [1,2,2,3,5,6]

#Initilize two pointers at the end of the arrays, m and n
#compare the two elements, whatever is the graters put it in the las poistion of nums 1

def mergeSortedArrays(nums1,m,nums2,n):
    last = len(nums1) - 1
    while m - 1 >= 0 and n -1 >= 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[last] =  nums1[m-1]
            m -= 1  
        else:
            nums1[last] = nums2[n-1]
            n -= 1
        last -= 1
    
    while n >= 0:
        nums1[last] = nums1[n]
        n -= 1
        last -= 1
    # If there are still elements in nums1 (m >= 0) after the main loop, there's no need to do anything with them. They are already in place.
    return nums1


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

mergeSortedArrays(nums1, m, nums2, n)

