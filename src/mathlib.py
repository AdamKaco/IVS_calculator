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
def mul(a, b):
    return (a * b)

#-------------------------------------------
# Name: division
# Brief: Divides numbers a and b
# exception: If b = 0, a ZeroDivisionError is activated           
# Return: If c does not contains a number, return x / y
#         If c contains a number, return x / y rounded to c decimal places
#-------------------------------------------
def div(a, b):
    if(b == 0):
        raise ZeroDivisionError
    
    return (a / b)


#-------------------------------------------
# Name: Exponentiation
# Brief: Calculate power of number to exponent (num^exp) 
# Return: If c does not contains a number, return result (num^exp)
#         If c contains a number, return result (num^exp) rounded to c decimal places
#-------------------------------------------
def exp(num, exp):
    result = 1
    if (exp == 0):
        return 1

    if isinstance(exp, int):
        pass
    elif (not exp.is_integer()):
        raise TypeError
    if (num == 0):
        return 0
    neg = 0
    if (exp < 0):
        exp = abs(exp)
        neg = 1
    
    result = num ** exp
    if (neg == 1):
        return div(1, result)
    else:
        return result
    

#-------------------------------------------
# Name: Square root
# Brief: Calculate root of number to nth-root (num^1/n)
# exception: If number < 0, a Exception is activated
# Return: If c does not contains a number, return result (num^1/n)
#         If c contains a number, return result (num^1/n) rounded to c decimal places
#-------------------------------------------
def root(num, n):
    if(num < 0 and n%2 == 0):
        raise TypeError
    elif isinstance(n, int):
        pass  
    elif (not n.is_integer()):
        raise TypeError

    if (n <= 0):
        raise ValueError #REMEMBER ME LATER
    result = num ** (1/n)
    
    return result

#-------------------------------------------
#
#
#-------------------------------------------
def fact(num):
    ans = 1
    if (num < 0):
        raise TypeError
    else:
        for i in range(1, num+1):
            ans = ans * i
    return ans
#-------------------------------------------
#
#
#-------------------------------------------
def comb (n, k):
    return n