"""
1822. Sign of the Product of an Array

There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).

Example 1:

Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1
"""

nums = [-1,-2,-3,-4,3,2,1]
nums = [1,5,0,2,-3]
nums = [-1,1,-1,1,-1]

def product(nums):
    total_product = nums[0]
    for i in range(1,len(nums)):
        (total_product) *= (nums[i])
    
    if total_product == 0:
        return 0
    elif total_product < 1:
        return -1
    else:
        return 1
    
#This solution could potencially lead to errors because some programming lengauges can only support 32bytes of integers so if the product result in a very large number this could potencilly return an error
    
# a better way to do this is to count the number of negative, is their odd the we return -1 if its even then 1, when there is one cero in nums we return 0. Key here is to identify that we do not need to return the product, and that every time we encounter a negetaive number this changes the sign of our result.

def signProduct(nums):
    number_negative = 0
    for i in nums:
        if i == 0:
            return 0
        elif i < 0:
            number_negative += 1
    
    return (1 if number_negative%2==0 else -1)
    
nums = [-1,-2,-3,-4,3,2,1]
signProduct(nums=nums)
