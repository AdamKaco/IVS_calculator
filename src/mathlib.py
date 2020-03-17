##
# @file mathlib.py
# @autor Peter Baris
# @date 07.03.2020
# @brief Math library for team project IVS_Calculator
#        Math operations: +,-,*,/,^,√,!,C
#

##
# @name Addition
# @brief Sum of two numbers a and b
# @return a + b
##@{
def sum(a, b):
    return a + b 
##@}

##
# @name Subtraction
# @brief Subtracts of two numbers a and b
# @return a - b
##@{
def sub(a, b):
    return a - b
##@}
 
##
# @name Multiplication
# @brief Multiplies numbers a and b
# @return a * b         
##@{
def mul(a, b):
    return (a * b)
##@}

##
# @name division
# @brief Divides numbers a and b
# @exception If b = 0, a ZeroDivisionError is activated           
# @return a / b
##@{
def div(a, b):
    if(b == 0):
        raise ZeroDivisionError
    
    return (a / b)
##@}

##
# @name Exponentiation
# @brief Calculate power of number to exponent (num^exp)
# @exception If exp is not integer, a TypeError is activated
#            If num = 0 and exp <= 0, a ValueError activated
# @return If exp = 0, return 1 or if num = 0, return 0
#         If exp < 0, return 1 / (num^(-exp))
#         If exp > 0, return result (num^exp)
##@{
def exp(num, exp):
    result = 1
    if isinstance(exp, int):
        pass  
    elif (not exp.is_integer()):
        raise TypeError

    if ((num == 0) and (exp < 0)):
        raise ValueError
    elif (exp == 0):
        return 1
    elif (num == 0):
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
##@}    

##
# @name Square root
# @brief Calculate root of number to nth-root (num^1/n)
# @exception If n is not integer, a TypeError is activated
#            If number < 0, a ValueError is activated
#            If num = 0 and n < 0, a ValueError is activated
# @return result (num^1/n)
# @{
def root(num, n):
    if isinstance(n, int):
        pass  
    elif (not n.is_integer()):
        raise TypeError

    if(num < 0 and n%2 == 0):
        raise ValueError
    elif((num == 0) and (n < 0)):
        raise ValueError

    if(num < 0):
        num = abs(num)
        result = -(num ** (1/n))
        return result
    else:
        result = num ** (1/n) 
        return result
##@}

##
# @name Factorial
# @brief Calculate factorial from number num 
# @exception If num is not intiger, a TypeError is activated
#            If num < 0, a ValueError is activated
# @return ans (num!)
##@{
def fact(num):
    ans = 1
    
    if isinstance(num, int):
        pass  
    elif (not num.is_integer()):
        raise TypeError 
    if (num < 0):
        raise ValueError
        
    else:
        for i in range(1, num+1):
            ans = ans * i
    return ans
##@}

##
# @name Combination
# @brief Calculate combinations k-th class from n elements
# @exception If n or k are not integer, a TypeError is activated
#            If n or k are < 0, a ValueError is activated
#            If (n - k) < 0, a ValueError is activated 
# @return result (fact(n) / (fact(k) * fact(n - k)))
#         If k = 0 or k = n, return 1
#         If k = 1, return 1
##@{
def comb (n, k):
    if isinstance(n, int):
        pass  
    elif (not n.is_integer()):
        raise TypeError       
    if isinstance(k, int):
        pass  
    elif (not k.is_integer()):
        raise TypeError
        
    if (n < 0):
        raise ValueError
    elif (k < 0):
        raise ValueError
    elif (k > n):
        raise ValueError
    elif ((n - k) < 0):
        raise ValueError
    
    if (k == 0):
        return 1
    elif (k == n):
        return 1
    elif (k == 1):
        return n
    
    result = (fact(n) / (fact(k) * fact(n - k))) 
    return result
 ##@}
