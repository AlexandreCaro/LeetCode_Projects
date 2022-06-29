from itertools import permutations

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dictionary_letters = {2: list('abc'), 3: list('def'), 4: list("ghi"), 5: list("jkl"), 6: list("mno"), 7:list("pqrs"), 8: list("tuv"), 9: list("wxyz")}
        
        if digits=="":
            
            return []
        
        print(dictionary_letters[2])
        
        list_strings = list()
        
        for digit in digits:
            
            print("digit", digit)
            
            list_strings.append(dictionary_letters[int(digit)])
            
#             for letter in list_digit:
                
#                 if letter not in list_strings:
                    
#                     list_strings.append(letter)
                    
#                 elif letter in liste_strings:
                    
#                     liste_strings[liste_strings.index(letter)] += letter

            final_list = list(itertools.product(*list_strings))
    
        liste_string_final = list()
                    
        for couple in final_list:
            
            str1 = ""
            
            str1 = str1.join(couple)
            
            liste_string_final.append(str1)
            
        return liste_string_final
            