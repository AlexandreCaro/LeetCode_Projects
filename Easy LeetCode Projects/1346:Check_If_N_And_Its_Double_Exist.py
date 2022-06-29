#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 08:56:04 2022

@author: alexandre
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        arr.sort()
        
        middle = len(arr)//2
        
        start, end = 0, len(arr)-1
        
        print(arr)
        
        list_zeros = list()
        
        for value in arr:
            
            if value==0:
                
                list_zeros.append(value)
                
                if len(list_zeros)>1:
                    
                    return True
                
                continue
            
            if arr[-1]<value*2:
                
                continue
                
            elif arr[-1]>=value*2:
                
                start, end = 0, len(arr)-1
                
                while start<=end:
                    
                    #print(middle)
                    
                    middle = (start+end)//2
                    
                    if arr[middle]==2*value:
                        
                        return True
                    
                    elif arr[middle]<2*value:
                        
                        start = middle+1
                        
                    elif arr[middle]>2*value:
                        
                        end = middle-1
                        
        return False
    
"""Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
Example 2:

Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.
Example 3:

Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.
 

Constraints:

2 <= arr.length <= 500
-10^3 <= arr[i] <= 10^3"""

input1 = [10,2,5,3]

input2 = [-10,12,-20,-8,15]

input3 = [-2,0,10,-19,4,6,-8]