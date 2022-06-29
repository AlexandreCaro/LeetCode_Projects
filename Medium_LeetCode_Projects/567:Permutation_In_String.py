#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 11:46:08 2022

@author: alexandre
"""

from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n = len(s1)
        
        if len(s1)>len(s2):
            
            return False
        
        if n==1:
            
            if s1 in s2:
                
                return True
            
            else:
                
                return False
            
        if len(s1)==len(s2) and "".join(sorted(s1))=="".join(sorted(s2)):
            
            return True
            
        if n<7:
        
            perms = [''.join(p) for p in permutations(s1, r=n)]

            set_perm = set(perms)

            for perm in set_perm:

                if perm in s2:

                    print(perm)

                    return True

            return False
        
        start, end = 0, len(s1)
        
        if s1 in s2:
            
            return True
        
        s1 = "".join(sorted(s1))
        
        while end<len(s2)-1:

            substring = s2[start:end]
            
            #print(len(substring), len(s1))

            start, end = start+1, min(start+1+len(s1), len(s2)-1)

            substring = "".join(sorted(substring))
            
            #print(substring)

            if substring==s1:

                return True

        return False
    
"""Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters."""
    