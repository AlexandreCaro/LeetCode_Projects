#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 12:02:33 2022

@author: alexandre
"""

import numpy as np

class Solution:
    def specialArray(self, nums) -> int:
        
        list_nums = list()
        
        nums_copy = np.array(copy.deepcopy(nums))
        
        n = len(nums)
        
        min_array = np.min(nums)
        
        max_array = np.max(nums)
        
        """x est nécessairement entre la longueur de l'array et l'élement maximpal de l'array."""
        
        minimum, maximum = min(min_array, n), max(n, max_array)
        
        #print(minimum, maximum)
        
        j = minimum
        
        while j<=maximum:
            
            if len(nums_copy[nums_copy>=j])==j:
                
                return j
            
            #print(j, nums_copy[nums_copy>=j])
            
            j+=1
        
        return -1
    
"""You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

 

Example 1:

Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.
Example 2:

Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.
If x = 0, there should be 0 numbers >= x, but there are 2.
If x = 1, there should be 1 number >= x, but there are 0.
If x = 2, there should be 2 numbers >= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums."""