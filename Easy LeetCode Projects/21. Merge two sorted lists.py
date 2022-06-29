#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class LinkedList:
    
    def __init__(self, head=None):
        self.head=head
    
    def append(self, value):
        current = self.head
        if self.head:
            while current.next:
                current=current.next
            current.next = ListNode(value)
        else:
            self.head = ListNode(value)
            
    def insertAfter(self, prev_node, new_data):
        
        new_node = ListNode(new_data)
        
        new_node.next = prev_node.next
        
        prev_node.next = new_node
        
def newNode(data):
    
    new_node = ListNode(data)
    new_node.val = data
    new_node.next = None
    return new_node

def insertEnd(head,data):
    
    if head==None:
        
        return newNode(data)
    
    else:
        
        head.next = insertEnd(head.next, data)
    
    return head
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        current = list1
        
        current2 = list2
        
        liste1 = list()
        
        liste2 = list()
        
        while current is not None:
            
            liste1.append(current.val)
            
            current = current.next
            
        while current2 is not None:
            
            liste2.append(current2.val)
            
            current2 = current2.next
        
        liste1.extend(liste2)
        
        liste1.sort()
        
        if len(liste1)==0:
            
            return list1
        
        ll = ListNode(liste1[0])
        
        for i in range(1, len(liste1)):
            
            insertEnd(ll, liste1[i])
            
        return ll