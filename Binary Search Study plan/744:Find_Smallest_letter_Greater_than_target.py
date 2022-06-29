"""Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
 

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Example 3:

Input: letters = ["c","f","j"], target = "d"
Output: 'f'"""

import string

class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        
        alphabet_string = string.ascii_lowercase
        
        alphabet_list = list(alphabet_string)
        
        dict_alphabet = dict()
        
        for index, value in enumerate(alphabet_list):
            
            dict_alphabet[value] = index+1
            
        #print(dict_alphabet)
        
        target_number = dict_alphabet[target]
        
        dict_letters = dict()
        
        for letter in letters:
            
            dict_letters[letter] = dict_alphabet[letter]
            
        keys = list(dict_letters.keys())
        
        #print(keys)
        
        for key in keys:
            
            if dict_letters[key]>target_number:
                
                return key
        
        first_letter = keys[0]
        
        return first_letter