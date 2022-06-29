# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        
        current1, current2 = l1, l2
        
        list_val_1, list_val_2 = list(), list()
        
        while current1:
            
            list_val_1.append(current1.val)
            
            current1=current1.next
            
        while current2:
            
            list_val_2.append(current2.val)
            
            current2 = current2.next
            
        list_val_1.reverse()
        
        list_val_2.reverse()
        
        print(list_val_1, list_val_2)
        
        string1, string2 = "", ""
        
        for number in list_val_1:
            
            string1+= str(number)
            
        for number in list_val_2:
            
            string2 += str(number)
            
        number1, number2 = int(string1), int(string2)
        
        type(number1)
        
        somme = number1+number2
        
        somme_string = str(somme)
        
        somme_string = somme_string[::-1]
        
        print(somme_string)
        
        ll_return = ListNode(int(somme_string[0]))
        
        head = ll_return
                             
        j = 1
                             
        while j<len(somme_string):
            
            ll_return.next = ListNode(int(somme_string[j]))
            
            ll_return = ll_return.next
            
            j+=1
                             
        return head
    
"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros."""