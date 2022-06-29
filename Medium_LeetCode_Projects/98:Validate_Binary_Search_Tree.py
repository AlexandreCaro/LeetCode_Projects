# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def preOrderTraversal(root):
            
            res = []
            
            if root:
                
                res = res + preOrderTraversal(root.left)
                
                res.append(root.val)
                
                res = res + preOrderTraversal(root.right)
                
            return res
        
        liste = preOrderTraversal(root)
        
        liste_sorted = sorted(liste)
        
        set_dup = set(liste)
        
        if len(set_dup)!=len(liste):
            
            return False
        
        return liste==liste_sorted
    
"""Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1"""

"""Runtime: 58 ms, faster than 57.33% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 17.5 MB, less than 14.00% of Python3 online submissions for Validate Binary Search Tree.
"""