from sys import getsizeof

class Solution:
    def reverse(self, x: int) -> int:
        
        list_limit = [-2,147,483,648, 2,147,483,647]
        
        if len(str(x))==1:
            
            return x
        
        s = str(x)
        
        j = len(s)-1
        
        while s[j]=='0':
            
            s.replace(s[j], '')
            
            j-=1

        s = s[::-1]
        
        if s[-1]=='-':
            
            new_string = s[:-1]
            
            negative_string = '-' + new_string
            
            y = int(negative_string)
            
            size = getsizeof(y)
        
            print(size)

            print(y < list_limit[0])

            if size<32:

                return y

            elif size==32:

                if abs(y)<2**31 and y!=2**31-1:

                    return y

                return 0

            elif size>32:

                return 0
        
        y = int(s)
        
        size = getsizeof(y)
        
        print(size)
        
        print(y < list_limit[0])
        
        if size<32:
            
            return y
        
        elif size==32:
            
            if abs(y)<2**31 and y!=2**31-1:
                
                return y
            
            return 0
        
        elif size>32:
            
            return 0
        
input1 = -2147483648
input2 = -2147483412

"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1"""

"""Runtime: 43 ms, faster than 56.05% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.9 MB, less than 65.11% of Python3 online submissions for Reverse Integer."""