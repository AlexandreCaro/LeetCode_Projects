"Here we use the Depth First search technique on a 2D array."

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        
        m, n = len(image), len(image[0])
        
        element_color = image[sr][sc]
        
        dRow = [0, 1, 0, -1]
        dCol = [-1, 0, 1, 0]
        
        boolean_array = [[False]*n for i in range(m)]
        
        def isValid(x, y):
            
            if (x < 0 or col <0 or x>=m or y >=n):
                
                return False
            
            if boolean_array[x][y]:
                
                return False
            
            if image[x][y]!=element_color:
                
                return False
            
            return True
        
        s = []
        
        s.append([sr, sc])
        
        while len(s)>0:
            
            curr = s[len(s)-1]
            
            s.remove(s[len(s)-1])
            
            row, col = curr[0], curr[1]
            
            if isValid(row, col)==False:
                
                continue
                
            if image[row][col] == element_color:
                
                image[row][col] = newColor
                
            boolean_array[row][col] = True
            
            print(image[row][col], end = " ")
            
            for i in range(4):
                adjx = row + dRow[i]
                adjy = col + dCol[i]
                s.append([adjx, adjy])
                
        return image
    
"""An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

 

Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]
 

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], newColor < 216
0 <= sr < m
0 <= sc < n"""

"""Runtime: 81 ms, faster than 78.87% of Python3 online submissions for Flood Fill.
Memory Usage: 14.2 MB, less than 39.75% of Python3 online submissions for Flood Fill."""