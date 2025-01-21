# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

 

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

#Create a variable that stores the result of the sum of of the square of the digits
#Create a while loop that works untile result is not equal to on
#in the while loop we're going to take the digits of result and calculated the sum squeare then update the result varaible

def happyNumber(number):
    res = number
    while res != 1:
        