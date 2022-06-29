"""Regex solution 144/176"""

from itertools import permutations
import re
import collections

class Solution:
    def findSubstring(self, s: str, words):
        
        list_words = list()
        
        list_index = list()
        
        temp = permutations(words)
        
        for i in list(temp):
            
            string = ""
            
            for j in i:
                
                string+=j
                
            list_words.append(string)
        
        print(list_words)
        
        for word in list_words:
            
            liste = [m.start() for m in re.finditer(word, s)]
            
            print(liste)
            
            list_index.extend(liste)
                
        return list(set(list_index))
    
"""Fist Solution 139/176"""

class Solution_First:
    def findSubstring(self, s: str, words):
        
        list_words = list()
        
        list_index = list()
        
        temp = permutations(words)
        
        for i in list(temp):
            
            string = ""
            
            for j in i:
                
                string+=j
                
            list_words.append(string)
        
        print(list_words)
        
        for word in list_words:
            
            while word in s and s.index(word) not in list_index:
                
                list_index.append(s.index(word))
                
                
        return list(set(list_index))
    
"""Second Solution 151/176"""

class Solution_Second:
    def findSubstring(self, s: str, words):
        
        list_words = list()
        
        list_index = list()
        
        temp = permutations(words)
        
        for i in list(temp):
            
            string = ""
            
            for j in i:
                
                string+=j
                
            list_words.append(string)
        
        print(list_words)
        
        list_index_2 = list()
        
        len_valid_substring = len(words)*len(words[0])
        
        for i in range(len(s)):
            
            if s[i:i+len_valid_substring] in list_words:
                
                list_index_2.append(i)
            
        print("2",list_index_2)
                
        return list_index_2
    


class draft:
    def findSubstring(self, s: str, words):
        
        list_words = list()
        
        list_index = list()
        
        temp = permutations(words)
        
        ones = [1]*len(words)
        
        dict_letters = dict(zip(words, ones))
        
        len_valid_substring = len(words[0])
        
        count = 0
        
        for i in range(len(s), len_valid_substring):
            
            if s[i:i+len_valid_substring] in words:
                
                dict_letters[s[i:i+len_valid_substring]] = 0
                
                count+=1
                
class Solution_corr:
    def findSubstring(self, s: str, words):
        
        n = len(s)
        
        k = len(words)
        
        ones = [1]*k
        
        wordLength = len(words[0])
        
        substringSize = wordLength * k
        
        wordCount = collections.Counter(words)
        
        def check(i):
            
            remaining = wordCount.copy()
            
            wordsUsed = 0
            
            for j in range(i, i+substringSize, wordLength):
                
                sub = s[j: j+wordLength]
                
                if sub in remaining:
                    
                    if remaining[sub]>0:
                        
                        remaining[sub] -= 1
                        
                        wordsUsed += 1
                        
                    else:
                        
                        break
                    
            if wordsUsed==k:
                
                return True
            
            else:
                
                return False
            
        list_index = list()
            
        for i in range(n-substringSize+1):
            
            if check(i):
                
                list_index.append(i)
                
        return list_index
    
"""Runtime: 785 ms, faster than 44.42% of Python3 online submissions for Substring with Concatenation of All Words.
Memory Usage: 14.1 MB, less than 80.27% of Python3 online submissions for Substring with Concatenation of All Words."""
    
"""You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
 

Constraints:

1 <= s.length <= 104
s consists of lower-case English letters.
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] consists of lower-case English letters."""
    
