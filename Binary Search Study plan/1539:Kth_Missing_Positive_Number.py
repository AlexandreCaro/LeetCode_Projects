"""
Created on Sun Apr 24 08:25:02 2022

@author: alexandre

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
"""

class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        
        n = arr[-1]
        
        list_missing = list()
        
        for i in range(1,n):
            
            if i not in arr:
                
                list_missing.append(i)
                
        if k>len(list_missing):
            
            for i in range(n+1, k+n+1):
                
                list_missing.append(i)
                
        print(list_missing)
                
        return list_missing[k-1]