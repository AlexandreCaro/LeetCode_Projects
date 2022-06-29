import numpy as np

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            
            return 0
        
        liste = sorted(nums)
        
        n = len(nums)
        
        count = 1
        
        maximum = 1
        
        liste_max = list()
        
        for i in range(n):
            
            if i < n-1:
            
                if liste[i+1]==liste[i]+1:
                    
                    #print("Got it!", i,count)

                    count+=1

                elif liste[i+1]!=liste[i]:
                    
                    liste_max.append(count)

                    if maximum < count:
                        
                        maximum = count
                        
                    count = 1
                    
            else: 
                
                liste_max.append(count)
            
        maximum = np.max(liste_max)
        
        return maximum
    
"""Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9"""

"""Runtime: 578 ms, faster than 43.32% of Python3 online submissions for Longest Consecutive Sequence.
Memory Usage: 45 MB, less than 5.01% of Python3 online submissions for Longest Consecutive Sequence."""

class Solution_cor:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)