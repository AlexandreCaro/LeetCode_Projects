# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedArrayToBST(self, nums):
        
        if len(nums)==1:
            
            root = TreeNode(nums[0])
            
            return root
        
        if len(nums)==2:
            
            root = TreeNode(nums[1])
            
            root.left = TreeNode(nums[0])
            
            return root
        
        mid = len(nums)//2
        
        root = TreeNode(nums[mid])
        
        root_primitive = root
        
        print(root)
        
        j  = mid-1
        
        while j >= 0:
            
            root.left = TreeNode(nums[j])
            
            root = root.left
            
            j -= 1
            
        root = root_primitive
        
        print("root3", root)
        
        i = len(nums)-1
        
        root.right = TreeNode(nums[i])
        
        root = root.right
        
        i-=1
        
        while i > mid:
            
            root.left = TreeNode(nums[i])
            
            root = root.left
            
            i -= 1
            
        print(root_primitive)
            
        return root_primitive