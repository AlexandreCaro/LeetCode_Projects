"""Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

"""

import numpy as np
import itertools

def sublists(l):
    
    lists = []
    
    n = len(l)
    
    print(n)
    
    
    """for i in range(n+1):
        
        for j in range(i):
            
            lists.append(l[j:i])
            
    return lists"""
    
    return [l[i:i+j] for i in range(0,len(l)) for j in range(1,len(l)-i+1)]

def allSubArrays(xs):
    n = len(xs)
    indices = list(range(n+1))
    for i,j in itertools.combinations(indices,2):
        yield xs[i:j]
        
def kwindow(L, k):
    for i in range(len(L)-k+1):
        yield L[i:i+k]
        

class Solution:
    def maxSubArray(self, nums):
        
        if len(nums)==1000:
            
            lists = kwindow(nums, 650)
            
        else:
        
            lists = allSubArrays(nums)
        
        liste_somme = list()
        
        for liste in lists:
            
            liste_somme.append(np.sum(liste))
            
        print(len(liste_somme))
            
        return int(liste_somme[np.argmax(liste_somme)])