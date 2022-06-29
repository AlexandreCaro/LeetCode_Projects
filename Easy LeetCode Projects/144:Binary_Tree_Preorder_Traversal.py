# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        
        res = []
        
        if root:
            
            res.append(root.val)
            
            res = res + self.preorderTraversal(root.left)
            
            res = res + self.preorderTraversal(root.right)
        
        return res
    
"""Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100"""

"""Runtime: 47 ms, faster than 35.00% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 13.9 MB, less than 59.50% of Python3 online submissions for Binary Tree Preorder Traversal."""
        