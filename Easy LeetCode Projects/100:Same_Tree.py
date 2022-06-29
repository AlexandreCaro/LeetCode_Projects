# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        
        visited = set()
        
        list_p = list()
        
        list_q = list()
        
        def dfs(visited, node, liste):

            if node not in visited:

                print(node)
                
                visited.add(node)
                
                liste.append(node.val)
                
                if node.left:
                
                    return dfs(visited, node.left, liste)
                
                else:
                    
                    liste.append(None)
                
                if node.right:
                    
                    return dfs(visited, node.right, liste)
                
                else:
                    
                    liste.append(None)
                    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_br:
    def isSameTree(self, p, q) -> bool:
        
        visited = set()
        
        liste = list()
        
        def printPreOrder(node, liste):
            
            if node:
                
                print(liste)
                
                liste.append(node.val)
                
                if node.left is None:
                    
                    liste.append(None)
                
                printPreOrder(node.left, liste)
                
                printPreOrder(node.right, liste)
                
            return liste
                    
        return printPreOrder(p, liste)
    
"56/60 Test Cases"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution3:
    def isSameTree(self, p, q) -> bool:
        
        visited = set()
        
        liste = list()
        
        def preorderTraversal(root):
            
            res = []
            
            if root:
                
                res.append(root.val)
                
                res = res + preorderTraversal(root.left)
                res = res + preorderTraversal(root.right)
                
                if root.left is None:
                
                    res.append(None)
                
                if root.right is None:
                
                    res.append(None)
                
            return res
        
        listp = preorderTraversal(p)
        
        listq = preorderTraversal(q)
        
        print(listp, listq)
        
        return listp == listq
    
"Solution"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_cor:
    def isSameTree(self, p, q) -> bool:
        
        if not p and not q:
            
            return True
        
        if not q or not p:
            
            return False
    
        if p.val != q.val:
            
            return False
        
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
    
    
"""Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104"""

"""Runtime: 39 ms, faster than 59.37% of Python3 online submissions for Same Tree.
Memory Usage: 14 MB, less than 29.64% of Python3 online submissions for Same Tree."""

"Iterative Solution"

from collections import deque

class Solution_iter:
    def isSameTree(self, p, q):
        
        def check(p, q):
            
            if not p and not q:
                
                return True
            
            if not q or not p:
                
                return False
            
            if p.val != q.val:
                
                return False
            
            return True
        
        deq = deque([(p, q),])
        
        while deq:
            
            p, q = deq.popleft()
            
            if not check(p, q):
                
                return False
            
            if p:
                
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
                
        return True
                
                