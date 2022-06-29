class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        liste = list(num)
        
        n = len(num)
        
        liste_numbers = liste[:k+1]
        
        liste_numbers = sorted(liste_numbers)
        
        j = 0
        
        print(liste_numbers)
        
        while j< k:
            
            liste_numbers.pop()
            
            j += 1
            
        liste_numbers = liste_numbers + liste[k+1:]
        
        string = "".join(liste_numbers)
        
        if string.startswith("0"):
            
            string = string.lstrip("0")
            
        if string=="":
            
            string += "0"
        
        return string