"""
1304. Find N Unique Integers Sum up to Zero
Given an integer n, return any array containing n unique integers such that they add up to 0.

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

Input: n = 3
Output: [-1,0,1]

Input: n = 1
Output: [0]
# """
def findUnique(n):
    res = []
    if n%2 != 0 :
        res.append(0)
    for i in range(0, n//2 + 1):
        res.append(i)
        res.append(-i)

#The key here to solve this problem is to indentify the following patterns, with odd numbers we just have to have a 0 and the add pairs of integers that are negative of each other, for example for 5, you can create the following array [-2,-1,0,1,2]
#when we have an even number we do the the same without the 0, for example for 4, [-2,-1,1,2]
#When implemented the solution you create an if-statement to add the cero when is odd. and then you loop with a for loop from 0 to n//2 + 1, you just need n divided by 2 to get the result, we add the one becase the range() function does not count the last one, and when n is add the result of the division is rounded to the floor 3//2 is 1.
n = 1
findUnique(n)
#Sliding window techinque, key here to identify this is that we are moving in a sublist of size n

# def find(n):
#     current_sum = 0
#     for position, value in enumerate(range(-n,n+1)):
#         if position <= n - 1:
#             current_sum += value
#         else:
#             current_sum -= 

# for value, position in enumerate(range(-1,1)):
#     print(value, position)