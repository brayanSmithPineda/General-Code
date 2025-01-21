"""
2259. Remove Digit From Number to Maximize Result

You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number.

 
Example:

Input: number = "1231", digit = "1"
Output: "231"
Explanation: We can remove the first '1' to get "231" or remove the second '1' to get "123".
Since 231 > 123, we return "231".
"""
#Create a variable to store the maximum number
#Convert the string to a list.
#Loop the list and if digit = arr[i] then you remove that number and store in the maximun variable

def removeDigit(string, digit):
    max_number = '0'
    for i in range(len(string)):
        if string[i] == digit:
            current_number = string[:i] + string[i+1:]
            max_number = max(max_number,current_number)
    return max_number

number = "133235"
digit = "3"
removeDigit(number,digit)

#Key: you didn't know how to came up with maximun_number, you didn't how to campare them, so here you should create a temporary variable that stores the current sum, number, average of the iteration and create another variable to store the maximun, minimum, then you compare it in each iteration max_number = max(max_number, current_number), when you need to keep track of a max just create a variable