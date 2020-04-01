## @file mathlib.py
# @author Peter Baris
# @date 07.03.2020
# @brief Math library implementing the +, -, *, /, ^, √, !, C operations

## @brief Sum of two numbers
# @return a + b
def sum(a, b):
    return a + b 

## @brief Subtracts two numbers
# @return a - b
def sub(a, b):
    return a - b
 
## @brief Multiplies two numbers
# @return a * b         
def mul(a, b):
    return (a * b)

## @brief Divides two numbers
# @exception ZeroDivisionError if @p b equals 0           
# @return a / b
def div(a, b):
    if(b == 0):
        raise ZeroDivisionError
    
    return (a / b)

## @brief Performs exponentiation.
# @exception TypeError if @p exp is not an integer
# @exception ValueError if @p num equals 0 and @p exp <= 0 (cannot divide by zero)
# @return num^exp
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

## @brief Calculates the n-th root of a number
# @exception TypeError if @p n is not an integer
# @exception ValueError if @p num < 0 and @p n is even
# @exception ValueError if @p num = 0 and @p n < 0
# @exception ZeroDivisionError if @p n = 0
# @return num^1/n
def root(n, num):
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

## @brief Calculates factorial
# @exception TypeError if @p num is not aa integer
# @exception ValueError if @p num < 0
# @return num!
def fact(num):
    ans = 1
    
    if isinstance(num, int):
        pass  
    elif (not num.is_integer()):
        raise TypeError 
    if (num < 0):
        raise ValueError
        
    else:
        for i in range(1, int(num)+1):
            ans = ans * i
    return ans

## @brief Calculates the amount of combinations of choosing @p k elements from @p n
# @exception TypeError if @p n or @p k are not integers
# @exception ValueError if @p n or @p k are < 0
# @exception ValueError if @p n < @p k
# @return fact(@p n) / (fact(@p k) * fact(@p n - @p k))
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