"""
Input: 10
Output : 55
Explanation: Jut sum up all the natural numbers from 1 to 10, 1+2+3+4+5+6+7+8+9+10 = 55
"""
def sum_numbers(number):
    if number == 1 or number == 0:
        return number
    return sum_numbers(number - 1) + number

number = 10
sum_numbers(number)