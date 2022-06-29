# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution_br1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        listeA = list()
        
        listeB = list()
        
        currA = headA
        
        currB = headB
        
        while currA:
            
            
            listeA.append(currA.val)
            currA = currA.next
            
        while currB:
            
            listeB.append(currB.val)
            currB = currB.next
            
        diff = abs(len(listeA)-len(listeB))
            
        print(listeA, listeB)
        
        listeA_rev, listeB_rev = listeA[::-1], listeB[::-1]
        
        intersection_rev = list()
        
        index1 = 0
        index2 = 0
        while listeA_rev[index1]==listeB_rev[index2]:
            intersection_rev.append(listeA_rev[index1])
            index1+=1
            index2+=1
        
        intersection = intersection_rev[::-1]
        
        print(intersection)
        
        curr = headA
        
        while curr:
            
            if curr.val == intersection[0] and curr.next.val == intersection[1]:
                
                return curr
            
            curr = curr.next
            
        return None
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution_br2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        listeA = list()
        
        listeB = list()
        
        currA = headA
        
        currB = headB
        
        while currA:
            
            
            listeA.append(currA.val)
            currA = currA.next
            
        while currB:
            
            listeB.append(currB.val)
            currB = currB.next
            
        diff = abs(len(listeA)-len(listeB))
            
        print(listeA, listeB)
        
        listeA_rev, listeB_rev = listeA[::-1], listeB[::-1]
        
        intersection_rev = list()
        
        count = 0
        while listeA_rev[count]==listeB_rev[count]:
            intersection_rev.append(listeA_rev[count])
            count+=1
        
        indexA = len(listeA) - count
        indexB = len(listeB)-count
        
        print(indexA, indexB)
        
        intersection = intersection_rev[::-1]
        
        take = min(indexA, indexB)
        
        curr = headA if min(indexA,indexB)==indexA else headB
        
        k = 0
        
        while k<take:
            
            k+=1
            curr = curr.next
            
        if count == 0:
            
            return None
        
        return curr
            

        
#         curr = headA
        
#         while curr:
            
#             if curr.val == intersection[0] and curr.next.val == intersection[1]:
                
#                 return curr
            
#             curr = curr.next
            
#         return None