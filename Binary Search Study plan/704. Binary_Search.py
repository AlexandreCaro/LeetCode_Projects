"""Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity."""

class Solution:
    def search(self, nums, target):
        
        if target in nums:
            
            return nums.index(target)
        
        else:
            
            return -1
        
s1 = [-1,0,3,5,9,12], 9
s2 = [-1,0,3,5,9,12], 2