class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        quotient = 0
        
        print(dividend, divisor)
        
        if divisor>0:
        
            while dividend-divisor>0:

                dividend = dividend - divisor

                quotient+=1

            return quotient
        
        if divisor<0:
            
            while dividend+divisor>0:
                
                dividend = dividend + divisor
                
                quotient-=1
                
            return quotient