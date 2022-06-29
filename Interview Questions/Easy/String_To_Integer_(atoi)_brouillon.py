#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 13:51:44 2022

@author: alexandre
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        
        integer = ""
        
        for value in s:
            
            if len(integer)==0:
                
                if value==" ":

                    pass

                elif value=="+" or value=="-":

                    integer += value

                elif value.isdigit():

                    integer+=value

                elif value.isalpha():

                    return 0
                
            elif len(integer)>0:
            
                if value==" ":

                    pass

                elif value=="+" or value=="-":

                    integer += value

                elif value.isdigit():

                    integer+=value

                elif value.isalpha():

                    break
                    
        """We have to check for the condition 32-bit integer range."""
                
        
                
        return int(integer)