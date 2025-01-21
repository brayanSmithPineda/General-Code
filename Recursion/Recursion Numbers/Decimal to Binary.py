def decimal_to_binary(decimal):
    if decimal == 0 or decimal == 1:
        return str(decimal)
    
    return decimal_to_binary(decimal//2) + str(decimal%2)

decimal = 233

decimal_to_binary(decimal)