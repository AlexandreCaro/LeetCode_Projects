import copy

class Solution:
    def threeSum(self, nums):
        
        if len(nums)<=2:
            
            return []
        
        if all(v==0 for v in nums):
            
            return [[0,0,0]]
        
        n = len(nums)
        
        liste_triplets = list()
        
        for i in range(n):
            
            for j in range(i+1, n):
                
                for k in range(j+1, n):
                    
                    if nums[i]+nums[j]+nums[k]==0:
                        
                        liste_triplets.append([nums[i], nums[j], nums[k]])
                        
        liste_final = list()
        
        index_list = list()
                        
        for index, liste in enumerate(liste_triplets):
            
            list_sorted = sorted(liste)
            
            #print(list_sorted)
            
            if list_sorted in liste_final:
                
                index_list.append(index)
            
            liste_final.append(list_sorted)
            
        #print(liste_triplets, index_list)
            
        for index in index_list[::-1]:
            
            liste_triplets.pop(index)

        return liste_triplets
    
class Solution1():
    
    def threeSum(self, nums):
        
        set_of_nums = set()
        result_set = set()
        
        for i in range(len(nums)-1):
            
            if i>0:
                
                for j in range(i+1, len(nums)):
                
                    element_to_find = -1 * (nums[i]+nums[j])
                    
                    if element_to_find in set_of_nums:
                        
                        result_set.add(tuple(sorted(nums[i], nums[j], element_to_find)))
                    
            set_of_nums.add(nums[i])
            
        return list(result_set)
    
"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105"""


                    
