"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        n = len(citations)
        
        liste_good = list()
        
        liste_current = list()
        
        h_index = 0
        
        h_index_max = 0
        
        for value1 in citations:
            
            liste_good = list()
            
            h_index =  value1
        
            for value in citations:

                if value >= value1:

                    liste_good.append(value)
                        
            if len(liste_good) > len(liste_current) and h_index > h_index_max:
                
                h_index_max = h_index
                
                liste_current = liste_good[:]

        return h_index_max
    
"""

def hIndex(citations) -> int:
    
    n = len(citations)
    
    liste_good = list()
    
    liste_current = list()
    
    h_index = 0
    
    h_index_max = 0
    
    for value1 in citations:
        
        liste_good = list()
        
        h_index =  value1
    
        for value in citations:

            if value >= value1:

                liste_good.append(value)
                
        if len(liste_good)>=value1:
            
            liste_current.append((value1, len(liste_good)))
        
        print(liste_current)
            
        return liste_current
    
citations = [2, 1]
citations1 = [3,0,6,1,5]
                
#On doit faire une liste contenant tous les tuples contenant en premier élément les citations et combien
# d'élements dans la liste ont une valeur supérieure à cette citation. Dans l'exemple, on voit qu'il y a
# un seul élément supérieur ou égal à 2, et 1 est inférieur à 2, donc on ne retient pas 2. 

# Par contre, 1 est retenu car 2 éléments dans la liste ont une valeur supérieure ou égale à 1 et le nombre
# d'élements 2 est supérieur à 1.

"Solution"

class Solution:
    def hIndex(self, citations) -> int:
        
        return sum(p < q for p, q in enumerate(sorted(citations, reverse=True)))
    
"""Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return compute the researcher's h-index.

According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.

If there are several possible values for h, the maximum one is taken as the h-index.

 

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1
 

Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000"""

"""Runtime: 82 ms, faster than 9.83% of Python3 online submissions for H-Index.
Memory Usage: 14.1 MB, less than 71.66% of Python3 online submissions for H-Index."""