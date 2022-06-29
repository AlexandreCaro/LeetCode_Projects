#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 21:19:18 2022

@author: alexandre
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        
        val_dup = -1
        
        list_dup = list()
        
        if head is None:
            
            return current
        
        previous = current
        
        while current!=None:
            """
            if previous.val == current.val:
                
                previous.next = current.next
            """
            #print("previous", previous)
            
            #print("current", current)
            
            #print(previous.val, current.val)
            
            previous = current
            
            current = current.next
            
            if current==None:
                
                break
            
            if previous.val == current.val:
                
                val_dup = previous.val
                
                previous.next = current.next
                
                current = previous.next
                
        """
                
        current = head
        
        while current!=None:
                
                previous = current
                
                current = current.next
                
                if current is None:
                    
                    break
                    
                if previous.val == current.val:
                    
                    previous.next = current.next
        
        current = head
        
        if current.val == previous.val:
            
            current.next=None
            
        """
            
        return head