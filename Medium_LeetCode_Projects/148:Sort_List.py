# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head):
        
        current = head
        
        liste_val = list()
        
        while current:
            
            liste_val.append(current.val)
            current = current.next
            
        liste_val.sort()
            
        current = head
        
        count = 0
        
        while current:
            
            current.val = liste_val[count]
            count+=1
            
            current = current.next
            
        return head
    
"""Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105"""

"""Runtime: 353 ms, faster than 85.44% of Python3 online submissions for Sort List.
Memory Usage: 36.4 MB, less than 24.05% of Python3 online submissions for Sort List.
"""
