#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 08:30:19 2022

@author: alexandre
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        
        length = 0
        
        while current:
            
            current = current.next
            
            length += 1
            
        if length % 2 ==0:
            
            middle = length//2+1
            
        elif length%2==1:
            
            middle = length//2+1
            
        j = 1
        
        current = head
        
        while j<middle:
            
            current = current.next
            
            j+=1
            
        return current
    
"""Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
    
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one."""

"""Runtime: 20 ms, faster than 99.76% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 13.9 MB, less than 57.14% of Python3 online submissions for Middle of the Linked List."""