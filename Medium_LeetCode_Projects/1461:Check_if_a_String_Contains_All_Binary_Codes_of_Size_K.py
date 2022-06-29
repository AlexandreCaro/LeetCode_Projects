class Solution_br:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        def printAll(n):
            result = []
            stringSoFar = ''
            def printAllrec(stringSoFar, n, result):
                
                if n==0:
                    
                    result.append(stringSoFar)
                    if len(result)==(2):
                        return result
                    
                else:
                    
                    printAllrec((stringSoFar+"0"), n-1, result)
                    printAllrec((stringSoFar+"1"), n-1, result)
                    
            printAllrec(stringSoFar, n, result)
            return result
        
        liste = printAll(k)
        
        #print(liste)
        
        for binary in liste:
            
            #print(binary)
            
            if binary in s:
                
                pass
                
            else:
                
                return False
            
        return True
    
"Solution 1: Set"

class Solution_Set:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        need = 1 << k
        got = set()
        
        for i in range(k, len(s)+1):
            
            temp = s[i-k:i]
            print(temp)
            if temp not in got:
                got.add(temp)
                need -= 1
                if need == 0:
                    return True
                
        return False
    
"""Runtime: 561 ms, faster than 42.48% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
Memory Usage: 27.1 MB, less than 51.77% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K."""

"""Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

 

Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
Example 2:

Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
Example 3:

Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and does not exist in the array.
 

Constraints:

1 <= s.length <= 5 * 105
s[i] is either '0' or '1'.
1 <= k <= 20"""