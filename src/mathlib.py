#----------------------------------------------------------
# Name: MathLib
# Autor: Peter Baris
# Date: 07.03.2020
# description: Math library for team project IVS_Calculator
#              Math operations: +,-,*,/,^,√,
#----------------------------------------------------------

#-------------------------------------------
# Name: Addition
# Brief: Sum of two numbers a and b
# Return: a + b
#-------------------------------------------
def sum(a, b):
    return a + b 

#-------------------------------------------
# Name: Subtraction
# Brief: Subtracts of two numbers a and b
# Return: a - b
#-------------------------------------------
def sub(a, b):
    return a - b
 
#-------------------------------------------
# Name: Multiplication
# Brief: Multiplies numbers a and b
# return: If c does not contains a number, return a * b
#         If c contains a number, return a * b rounded to c decimal places          
#-------------------------------------------
def mul(a, b, c = False):
    if(c == False):
        return (a * b)
    else:
        return round(x * y, c)

#-------------------------------------------
# Name: division
# Brief: Divides numbers a and b
# exception: If b = 0, a ZeroDivisionError is activated           
# Return: If c does not contains a number, return x / y
#         If c contains a number, return x / y rounded to c decimal places
#-------------------------------------------
def div(a, b, c = False):
    if(b == 0):
        raise ZeroDivisionError
        
    if(c == False):
        return (a / b)
    else:
        return round(x / y, c) 

#-------------------------------------------
# Name: Exponentiation
# Brief: Calculate power of number to exponent (num^exp) 
# Return: If c does not contains a number, return result (num^exp)
#         If c contains a number, return result (num^exp) rounded to c decimal places
#-------------------------------------------
def pow(num, exp, c = False):
    result = pow(num, exp)
    
    if(c == False):
        return result
    else:
        return round(result, c)

#-------------------------------------------
# Name: Square root
# Brief: Calculate root of number to nth-root (num^1/n)
# exception: If number < 0, a Exception is activated
# Return: If c does not contains a number, return result (num^1/n)
#         If c contains a number, return result (num^1/n) rounded to c decimal places
#-------------------------------------------
def root(num, n, c = False):
    if(num < 0):
        raise Exception
    result = pow(num, 1/n)
    if(c == False):
        return result
    else:
        return round(result, c)

#-------------------------------------------
#
#
#-------------------------------------------

#-------------------------------------------
#
#
#-------------------------------------------