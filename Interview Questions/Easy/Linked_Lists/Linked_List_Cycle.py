# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        
        current = head
        
        if current is None:
            
            return False
        
        val_list1, val_list2 = list(), list()
        
        while current is not None:
            
            #print(current.val)
            
            current = current.next
            
            if current is None:
                
                break
            
            if current.val not in val_list1:
                
                val_list1.append(current.val)
                
            elif current.val in val_list1:
                
                val_list2.append(current.val)
                
            print(val_list1, val_list2)
            
            if len(val_list1)>=200:
                
                return False
                
            if all(elem in val_list1 for elem in val_list2) and len(val_list1)==len(val_list2):
                
                return True
            
            #print(val_list1, val_list2)
            
        return False
                
                
        
        """
        
        try:
        
            print(head)
            
        except:
            
            return True
        
        else:
            
            return False
            
        """
        