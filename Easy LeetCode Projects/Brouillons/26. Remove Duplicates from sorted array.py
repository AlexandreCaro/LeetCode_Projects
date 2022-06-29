#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 21:57:25 2022

@author: alexandre
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        liste_unique = list()
        
        count = 0
        
        s = set()
        
        for num in nums:
            
            print(num)
            
            if num not in s:
                
                s.add(num)
                
            elif num in s:
                
                nums.remove(num)
                
        return len(nums)