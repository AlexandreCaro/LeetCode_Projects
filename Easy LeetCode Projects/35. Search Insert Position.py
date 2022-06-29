"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity."""

class Solution:
    def searchInsert(self, nums, target):
        
        if target in nums:
            
            return nums.index(target)
        
        else:
            
            n = len(nums)//2
            
            print(n)
            
            if target>nums[n]:
                
                j=n
                
                while j<=len(nums)-1:
                    
                    print(j)
                    
                    if j==len(nums)-1:
                        
                        return len(nums)
                    
                    if nums[j]<target and nums[j+1]>target:
                        
                        return j+1
                    
                    j+=1
                
                for i in range(n,len(nums)-1):
                    
                    if target < nums[i] and target > nums[i-1]:
                        
                        nums.insert(i, target)
                        
                        return i
                        
            elif target<nums[n]:
                
                j=n
                
                while j>=0:
                    
                    if j==0:
                        
                        return 0
                    
                    print(j)
                    
                    if nums[j]>target and nums[j-1]<target:
                        
                        return j
                    
                    j-=1
                    
s1 = [1,3,5,6], 5
s2=  [1,3,5,6], 2
s3 = [1,3,5,6], 7