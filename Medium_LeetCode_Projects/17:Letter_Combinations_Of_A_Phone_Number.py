import itertools

class Solution:
    def letterCombinations(self, digits):
        
        dictionary_letters = {2: list('abc'), 3: list('def'), 4: list("ghi"), 5: list("jkl"), 6: list("mno"), 7:list("pqrs"), 8: list("tuv"), 9: list("wxyz")}
        
        if digits=="":
            
            return []
        
        print(dictionary_letters[2])
        
        list_strings = list()
        
        for digit in digits:
            
            print("digit", digit)
            
            list_strings.append(dictionary_letters[int(digit)])

            final_list = list(itertools.product(*list_strings))
    
        liste_string_final = list()
                    
        for couple in final_list:
            
            str1 = ""
            
            str1 = str1.join(couple)
            
            liste_string_final.append(str1)
            
        return liste_string_final
            
"""Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9']."""

"""Runtime: 33 ms, faster than 79.64% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13.9 MB, less than 79.68% of Python3 online submissions for Letter Combinations of a Phone Number."""