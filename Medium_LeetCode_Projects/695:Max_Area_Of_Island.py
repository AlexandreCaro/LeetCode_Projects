"The first solution uses a depth First Search recursive technique."

class Solution_rec(object):
    def maxAreaOfIsland(self, grid):
        
        seen = set()
        
        def area(r, c):
            
            if not(0<= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in seen
                   and grid[r][c]):
                
                return 0
            
            seen.add(r, c)
            
            return (1+area(r-1, c)+area(r+1, c) + area(r, c-1) + area(r, c+1))
        
        return max(area(r, c) for r in range(len(grid)) for c in range(len(grid[0])))



"The second solution uses the Depth First search iterative technique."

class Solution:
    def maxAreaOfIsland(self, grid):
        
        seen = set()
        ans = 0
        
        for r0, row in enumerate(grid):
            
            for c0, val in enumerate(row):
                
                if val and (r0, c0) not in seen:
                    
                    shape=0
                    stack = [(r0, c0)]
                    seen.add((r0,c0))
                    
                    while stack:
                        
                        r, c = stack.pop()
                        shape+=1
                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            
                            if (0<= nr <len(grid) and 0<= nc < len(grid[0])
                                and grid[nr][nc] and (nr, nc) not in seen):
                                
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                                
                    ans = max(ans, shape)
        
        return ans
    

    
"""You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1."""

"""class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        liste_iles = list() #C'est une liste contenant les iles qui sont sous forme de liste/
        
        liste_index = list() #C'est une liste contenant des listes contenant les tuples des localisations
                             # de chaque 1 qui a déjà été repertorié.
            
        liste_count = list()
        
        maximum = 0
        
        for i in range(m):
            
            for j in range(n):
                
                if grid[i][j]==1:
                    
                    index_x, index_y = i, j
                    
                    count = 1
                    
                    if index_x == m-1:
                        
                        break
                    
                    while grid[index_x+1][index_y]==1:
                        
                        index_x = index_x + 1
                        
                        count+=1
                        
                        while grid[index_x][index_y+1]==1:
                            
                            index_y = index_y + 1
                        
                            count+=1
                            
                        if index_x==m-1:
                            
                            break
                            
                    if count> maximum:
                        
                        maximum = count
                        
                          
        return maximum"""
    
"""class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        dRow = [0, 1, 0, -1]
        dCol = [-1, 0, 1, 0]
        
        boolean_array = [[False]*n for i in range(m)]
        
        def isValid(row, col):
            
            if (row < 0 or col < 0 or row>=m or col>=n):
                
                return False
            
            if (boolean_array[row][col]):
                
                return False
            
            return False
        
        s = []
        
        s.append([0,0])
        
        liste_somme = list()
        
        while len(s)>0:
            
            curr = s[len(s)-1]
            
            s.remove(s[len(s)-1])
            
            row, col = curr[0], curr[1]
            
            if isValid(row, col)==False:
                
                continue
                
            boolean_array[row][col]=True
            
            print(grid[row][col], end=" ")
            
            somme = 0
            
            for i in range(4):
                
                adjx = row + dRow[i]
                adjy = col + dCol[i]
                
                s.append([adjx, adjy])
                
                if grid[adjx][adjy] == 1:
                    
                    somme+=1
                
            liste_somme.append(somme)
            
        return liste_somme"""
    
"""class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        liste_iles = list() #C'est une liste contenant les iles qui sont sous forme de liste/
        
        liste_index = list() #C'est une liste contenant des listes contenant les tuples des localisations
                             # de chaque 1 qui a déjà été repertorié.
            
        liste_count = list()
        
        maximum = 0
        
        boolean_array = [[False]*n for i in range(m)]
        
        def isValid(row, col):
            
            if (row < 0 or col < 0 or row>=m or col>=n):
                
                print("Got it")
                
                return False
            
            if boolean_array[row][col]:
                
                print("Got it2")
                
                return False
            
            return True
        
        for i in range(m):
            
            for j in range(n):
                
                if grid[i][j]==1:
                    
                    boolean_array[i][j]=True
                    
                    index_x, index_y = i+1, j
                    
                    count = 1
                    
                    if isValid(index_x, index_y)==False:
                        
                        break
                    
                    boolean_array[index_x][index_y] = True
                    
                    while grid[index_x][index_y]==1:
                        
                        index_x = index_x + 1
                        
                        count+=1
                        
                        if isValid(index_x, index_y)==False:
                            
                            break
                            
                        boolean_array[index_x][index_y] = True
                        
                        while grid[index_x][index_y+1]==1:
                            
                            index_y = index_y + 1
                        
                            count+=1
                            
                            if isValid(index_x, index_y)==False:
                                
                                break
                                
                            boolean_array[index_x][index_y] = True
                            
                    if count> maximum:
                        
                        maximum = count
                        
        print(boolean_array)
                        
        return maximum"""