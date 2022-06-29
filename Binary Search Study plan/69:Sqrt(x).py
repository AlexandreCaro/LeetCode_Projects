"""Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned."""

class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x==0:
            
            return 0
        
        start, end = 1, x
        
        while start<=end:
            
            middle = (start+end)//2
            
            middle_bis = middle+1
            
            square = middle*middle
            
            square_bis = middle_bis*middle_bis
            
            #print(middle, middle_bis, square, square_bis)
            
            #print(square<x & square_bis>x)
            
            if (square<x and square_bis>x):
                
                return middle
            
            if square==x:
                
                return middle
            
            elif square>x:
                
                end = middle-1
                
            elif square<x:
                
                start = start+1