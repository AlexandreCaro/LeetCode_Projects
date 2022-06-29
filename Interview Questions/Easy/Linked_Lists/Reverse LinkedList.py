# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        
        val_list = list()
        
        if current is None:
            
            return current
        
        index = 1
        
        val_list.append(current.val)
        
        while current is not None:
            
            val_list.append(current.val)
        
            current = current.next
            
            index+=1
            
        val_list.reverse()
        
        current = head
        
        #print(current)
        
        index = 0
        
        while current is not None:
            
            current.val = val_list[index]
            
            current = current.next
            
            index+=1
            
        #print(current)
        
        return head
    
"""Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""