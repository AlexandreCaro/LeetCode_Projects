#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 07:59:14 2022

@author: alexandre
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        
        list_reverse = list()
        
        sentence = s.split(' ')
        
        for word in sentence:
            
            string = ""
            
            #print("word before", word)
            
            word = list(word)
            
            word.reverse()
            
            #print(word)
            
            string = string.join(word)
            
            list_reverse.append(string)
            
            #print(string)
            
        #print(list_reverse)
        
        string_reverse = " ".join(list_reverse)
        
        return string_reverse
    
"""Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space."""