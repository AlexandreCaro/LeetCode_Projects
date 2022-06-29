#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 08:40:47 2022

@author: alexandre
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        
        if head.next==None:
            
            head = None
            
            return head
        
        current = head
        
        length = 0
        
        while current:
            
            current = current.next
            
            length+=1
            
        index = length-n
        
        if index==0:
            
            return head.next
        
        current = head
        
        previous = current
        
        j = 0
        
        while j<index:
            
            previous = current
            
            current = current.next
            
            j+=1
            
        previous.next = current.next
        
        return head
    
"""Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1: Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]"""