def binary_search(arr, x):
    
    low_x, high_x = 0, len(arr)-1
    
    low_y, high_y = 0, len(arr[0])-1
    
    mid_x, mid_y = 0, 0
    
    while low_x<=high_x:
        
        mid_x = (high_x+low_x)//2
        
        if x >= arr[mid_x][0] and x <= arr[mid_x][-1]:
            
            break
        
        if x > arr[mid_x][0]:
            
            low_x = mid_x+1
            
        elif x < arr[mid_x][0]:
            
            high_x = mid_x-1
            
        elif x==arr[mid_x][0]:
            
            return True
        
    while low_y <= high_y:
        
        mid_y = (low_y+high_y)//2
        
        if x > arr[mid_x][mid_y]:
            
            low_y = mid_y+1
            
        elif x < arr[mid_x][mid_y]:
            
            high_y = mid_y-1
            
        elif x==arr[mid_x][mid_y]:
            
            return True
    
    return False
            
        

class Solution:
    def searchMatrix(self, matrix, target):
        
        return binary_search(matrix, target)
    
"""Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104"""