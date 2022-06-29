"""
Created on Sun Apr 24 08:29:33 2022

@author: alexandre

Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s.strip(" ")
        
        list_word = s.split(" ")
        
        print(list_word)
        
        last_word = list_word[-1]
        
        return len(last_word)