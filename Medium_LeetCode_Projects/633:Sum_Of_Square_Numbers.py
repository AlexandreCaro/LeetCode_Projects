import numpy as np

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        if c==0:
            
            return True
        
        max_number_i = int(np.sqrt(c))+1
        
        #print("max_number",max_number_i)
        
        somme = 0
        
        for i in range(1,max_number_i):
            
            somme = i**2
            
            #print("i",i)
            
            if somme==c:
                
                return True
            
            start, end = i, max_number_i
            
            while start<=end:
                
                somme = i**2
                
                middle = (start+end)//2
                
                #print("middle", middle)
                
                somme+=middle**2
                
                if somme==c:
                    
                    return True
                
                elif somme<c:
                    
                    start = middle+1
                    
                elif somme>c:
                    
                    end = middle-1
                    
        return False
    
"""Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
 

Constraints:

0 <= c <= 231 - 1"""