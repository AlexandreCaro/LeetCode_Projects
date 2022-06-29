"""Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109"""

import math

class Solution:
    def searchRange(self, nums, target: int):
        
        list_index = list()
        
        if target not in nums:
            
            return [-1, -1]
        
        if len(nums)==1:
            
            return [0,0]
        
        if len(set(nums))==1 and target in nums:
            
            return [0, len(nums)-1]
        
        if len(nums)<10:
            
            start = nums.index(target)
            
            list_index.append(start)
            
            for i in range(start, len(nums)):
                
                if i==len(nums)-1 and nums[i]==target:
                    
                    list_index.append(i)
                    
                    return list_index
                
                if nums[i]==target:
                    
                    pass
                
                else:
                    
                    list_index.append(i-1)
                    
                    return list_index
            
            list_index.append(start)
            
            return list_index
        
        start, end = 0, len(nums)-1
        
        max_iter = math.log2(len(nums))
        
        j=0
        
        while start<=end and j<max_iter:
            
            middle = (start+end)//2
            
            if end>target:
                
                end = middle-1
                
            elif start<target:
                
                start=middle+1
                
            j+=1
                
        while start<target:
            
            start+=1
            
        list_index.append(nums.index(start))
        
        index = list_index[0]
        
        while nums[index]==target:
            
            if index==len(nums)-1:
                
                list_index.append(index)
                
                return list_index
            
            index+=1
            
        list_index.append(index-1)
        
        return list_index