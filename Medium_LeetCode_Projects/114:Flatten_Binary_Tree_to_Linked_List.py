# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def preOrderTraversal(root):
            
            res = []
            
            if root:
                
                res.append(root.val)
                
                res = res + preOrderTraversal(root.left)
                
                res = res + preOrderTraversal(root.right)
                
            return res
        
        liste = preOrderTraversal(root)
        
        print(liste)
        
        root_primitive = root
        
        for value in liste[1:]:
            
            root.left = None
            
            root.right = TreeNode(value)
            
            root = root.right
            
        return root_primitive
    
"""Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""

"""Runtime: 36 ms, faster than 92.60% of Python3 online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 15.2 MB, less than 47.93% of Python3 online submissions for Flatten Binary Tree to Linked List."""