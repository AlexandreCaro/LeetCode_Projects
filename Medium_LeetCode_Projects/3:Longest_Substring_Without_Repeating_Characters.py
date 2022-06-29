class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        substring_list = list()
        
        string = ""
        
        n = len(s)
        
        if n==0:
            
            return 0
        
        if n==1:
            
            return 1
        
        if n==2 and s[0]!=s[1]:
            
            return 2
        
        maximum = 1
        
        print("n", n)
        
        for index, letter in enumerate(s):
            
            if index<n-1:
                
                index_letter=index+1
                
                #print(index_letter)

                string = letter

                count = 1

                while s[index_letter]!=letter and s[index_letter] not in string:

                    string += s[index_letter]

                    index_letter+=1

                    count+=1

                    if count>maximum:

                        maximum = count

                    if index_letter == n:

                        break
                        
                    #print("after", index_letter)

                substring_list.append(string)

            elif index == n-1:
                
                break
        
            
        return maximum
    
"""Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
Accepted
3,217,891
Submissions
9,740,332"""