from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def isSymmetric(self, root) -> bool:
        
        if root.left is None and root.right is None:
            
            return True
        
        node_left, node_right = root.left, root.right
        
        """On va faire un preorder traversal de chaque sous-arbre de droite et de gauche et on va
        inverser la list de l'arbre de droite et voir si c'est égal à celle issue de l'arbre de gauche"""
        
        """Pour que deux arbres soient miroirs l'un de l'autre il faut que le sous-arbre gauche de la racine de droite soit égal au sous-arbre de droite de la racine de gauche et vice-versa."""
        
        print(node_left, node_right)
        
        if node_left and node_right:
        
            if self.isSameTree(node_left.right, node_right.left) and self.isSameTree(node_left.left, node_right.right):
                
                print(node_left.right, node_right.left, node_left.left, node_right.right)

                return True
        
        return False
                
#         deq = deque([(node_left, node_right),])
        
#         while deq:
            
#             node_left, node_right = deq.popleft()
            
#             if not check(node_left, node_right):
                
#                 return False
            
#             if node_left.right.val == node_right.left.val and node_left.left.val == node_right.right.val:

#                 pass

#             else:

#                 return False
            
#             if node_left:
            
#                 deq.append((node_left.left, node_right.left))
#                 deq.append((node_left.right, node_right.right))
            
#         return True
        
    def preorderTraversal(self, root):

        res = []

        if root:

            res.append(root.val)

            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)

        return res
    
    def isSameTree(self, p, q) -> bool:
        
        if not p and not q:
            
            return True
        
        if not q or not p:
            
            return False
    
        if p.val != q.val:
            
            return False
        
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isMirror(self, root1, root2):
        
        if root1 is None and root2 is None:
            
            return True
        
        if root1 is not None and root2 is not None:
            
            if root1.val==root2.val:
                
                return (self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left))
            
        return False
        
    def isSymmetric(self, root) -> bool:
        
        return self.isMirror(root.left, root.right)
    
"""Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100"""

"""Runtime: 30 ms, faster than 96.53% of Python3 online submissions for Symmetric Tree.
Memory Usage: 14.1 MB, less than 22.02% of Python3 online submissions for Symmetric Tree."""