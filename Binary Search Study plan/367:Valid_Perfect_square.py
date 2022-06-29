"""Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
    
        def binarySearch(num):
            
            start = 1
            
            end = num
            
            while start<=end:
                
                print(start, end)
                
                middle = (start+end)//2
                
                square = middle**2
                
                #print(num, square)
                
                #print(square==num)
                
                if square==num:
                    
                    return True
                
                elif square<num:
                    
                    start = start+1
                    
                else:
                    
                    end = middle-1
                    
            return square==num
        
        return binarySearch(num)