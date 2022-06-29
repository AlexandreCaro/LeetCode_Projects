#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 21:19:54 2022

@author: alexandre
"""

class Solution:
    def strStr(self, haystack, needle):
        
        if needle=="":
            
            return 0
        
        if needle in haystack:
            
            return haystack.index(needle)
        
        else:
            
            return -1
        
s1 = "hello", "ll"
s2 = "aaaaa", "bba"

