#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 13:21:45 2022

@author: alexandre
"""

import numpy as np

class Solution:
    def search(self, nums, target):
        
#         if target in nums:
            
#             return nums.index(target)
    
#         else:
            
#             return -1

        n = len(nums)

        if n==1:
        
            if target == nums[0]:
                
                return 0
            
            else:
                
                return -1
            
        if n<10:
            
            if target in nums:
                
                return nums.index(target)
            
            else:
                
                return -1

        middle = np.argmin(nums)
    
        print(middle)
        
        if target == nums[middle]:
            
            return middle

        if target >= nums[0]:
            
            start, end = 0, middle-1
            
        elif target < nums[-1]:
            
            start, end = middle+1, len(nums)-1
            
        if target > nums[-1] and target < nums[0]:
            
            return -1
            
        while start<=end:
            
            print(middle)
            
            middle = (start+end)//2
            
            if nums[middle]> target:
                
                end = middle-1
                
            elif nums[middle]< target:
                
                start = middle + 1
                
            elif nums[middle]==target:
                
                return middle
            
        return -1
    
"""There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104"""