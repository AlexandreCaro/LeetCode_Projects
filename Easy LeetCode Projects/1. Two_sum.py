#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 07:47:24 2022

@author: alexandre
"""

def twoSum(nums, target):
    
        #print(target)
        
        liste_nombre = list()
        
        sum = 0
        
        for i in range(len(nums)):
            
            #print("i",nums[i])
            
            sum = nums[i]
            
            for j in range(i+1, len(nums)):
                
                #print("j", nums[j])
                
                sum+=nums[j]
                
                if sum==target:
                    
                    #print("je suis arrivé!")
                    
                    liste_nombre.extend([i,j])
                    
                    break
                    
                else:
                    
                    sum = nums[i]
                    
        return liste_nombre
    
nums, target = [2,7,11,15], 9
nums1, target1 = [3,2,4], 6
nums2, target2 = [3,2,3], 6
nums3, target3 = [-6, 1, 0, 4], -5