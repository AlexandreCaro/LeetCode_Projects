import numpy as np

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        list_palindrome = list()
        
        for index, letter in enumerate(s):
            
            #print(index, letter)
            
            j = index+1
            
            string = ""
            
            #print(s[index:j])
            
            while j < len(s):
                
                #print(s[index:j])
                
                temp = s[index:j]
                
                if temp == temp[::-1]:
                    
                    #print("Got it!")
                    
                    string = temp
                
                j += 1
                
                
            list_palindrome.append(string)
            
        list_len = [len(string) for string in list_palindrome]
        
        index_max = np.argmax(list_len)
        
        return list_palindrome[index_max]
    
"Deuxième version:"

class Solution2:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s)==1:
            
            return s
        
        string_max = ""
        
        if len(s)<15:
        
            for index, letter in enumerate(s):

                #print(index, letter)

                j = index+1

                string = ""



                #print(s[index:j])

                while j <= len(s):

                    #print(s[index:j])

                    temp = s[index:j]

                    if temp == temp[::-1]:

                        #print("Got it!")

                        string = temp

                        if len(string)>len(string_max):

                            string_max = string

                    j += 1
                    
            print(string_max)


    #             list_palindrome.append(string)

    #         list_len = [len(string) for string in list_palindrome]

    #         index_max = np.argmax(list_len)

            return string_max
    
        else:
            
            for index, letter in enumerate(s):

                #print(index, letter)

                j = index+1

                string = ""
                
                middle = (len(s)-j)//2

                #print(s[index:j])

                while j <= len(s):

                    #print(s[index:j])

                    temp = s[index:j]

                    if temp == temp[::-1]:

                        #print("Got it!")

                        string = temp

                        if len(string)>len(string_max):

                            string_max = string

                    j += 1
                    
            print(string_max)
            
            return string_max
        
"Solution 3:"

class Solution3:
    def longestPalindrome(self, s: str) -> str:
        
        def palindrome(string):
            string = string.lower().replace(' ', '')
            first, last = 0, len(string) - 1
            while(first < last):
                if(string[first] == string[last]):
                    first += 1
                    last -= 1
                else:
                    return False

            return True
        
        print(s[1:], s[:-1], s[1:-1])
        
        print(palindrome(s[1:]), palindrome(s[:-1]), palindrome(s[1:-1]))
        
        if len(s)==0:
            
            return ""
        
        if len(s)==2 and s!=s[::-1]:
            
            return s[0]
        
        if palindrome(s):
            
            return s
        
        if palindrome(s[1:]):
            
            return s[1:]
        
        if palindrome(s[:-1]):
            
            return s[:-1]
        
        if palindrome(s[1:-1]):
            
            return s[1:-1]
        
        list_candidates = [s[1:], s[:-1], s[1:-1]]
        
        #list_candidates = [s[x:y] for x in range(len(s)) for y in range(len(s))]
        
        for string in list_candidates:
            
            return self.longestPalindrome(string)
        
"""Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters."""