#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 21:12:28 2022

@author: alexandre
"""

class Solution:
    def removeElement(self, nums, val):
        
        while val in nums:
            
            nums.pop(nums.index(val))
            
        return len(nums)
    
s1 = [3,2,2,3], 3
s2 = [0,1,2,2,3,0,4,2], 2
