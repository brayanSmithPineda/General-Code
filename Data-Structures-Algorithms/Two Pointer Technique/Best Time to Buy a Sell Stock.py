# Best Time to Buy and Sell Stock

# Say you have an array for which the ith element is the price of a given stock on day i.
# if you were only permitted to complete at most one transaction (ie. buy one and sell one share of the stock), design and algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1.
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and seel on day 5 (price = 6), profit 6-1 = 5. Not 7-1, as selling price needs to be larger than buying price

#We need to find the minimun number and the maximun number so we get the maximum profit, we can do that by comparing each element and calculate the profit, we do not need to calculate for those values where the buy value is greter

#We set two pointer one will the buy pointer(left) and the other one is going to be the right pointer(sell pointer)
# we move left to the right in case right>left, that means we found a lower buy price
# we move right every single time one step at a time, so that way we can calculate de profit

#Create a variable the store the maximum profit, intilize to cero
#Crete the left pointer initialize at 0, first element
#loop throught the array (right pointer)
# if left> right, we update the value of left with right
# we also calculate the profit and if its greater than the maximun profit we save it

def maxProfit(arr):
    maximum_profit = 0
    left = 0
    for right in range(1,len(arr)):
        profit = arr[right] - arr[left]
        if arr[right] < arr[left]:
            left = right
        else:
            maximum_profit = max(profit, maximum_profit)
    return maximum_profit
arr = [7,1,5,3,6,4]
maxProfit(arr)





def MaximunProfit(arr):
    left = 0
    totalProfit = 0
    for right in range(1,len(arr)):
        if arr[left] > arr[right]:
            left = right
        else:
            totalProfit = max(arr[right] - arr[left],totalProfit)
    return totalProfit

arr = [7,1,5,3,6,4]
MaximunProfit(arr)

def MaximunProfit2(arr):
    left, right = 0,1
    totalProfit = 0
    while right < len(arr):
        if arr[left] > arr[right]:
            left = right
        else:
            totalProfit = max(arr[right] - arr[left],totalProfit)
        right += 1
    return totalProfit

arr = [7,1,5,3,6,4]
MaximunProfit2(arr)