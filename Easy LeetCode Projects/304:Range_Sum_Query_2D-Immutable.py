"Test cases: 17/24"

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        somme = 0
        
        #print((row1, col1), (row2, col2))
        
        for row in self.matrix[row1: row2+1]:
            
            for col in row[col1:col2+1]:
                
                somme += col
                
        return somme
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

"Solution:"

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.dp = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
        
        for r in range(len(self.dp)-1):
            
            for c in range(len(self.dp[0])-1):
                
                self.dp[r+1][c+1] = matrix[r][c] + self.dp[r][c+1] + self.dp[r+1][c] - self.dp[r][c]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

"""Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
 

Example 1:


Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-105 <= matrix[i][j] <= 105
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 104 calls will be made to sumRegion."""

"""Runtime: 2249 ms, faster than 43.72% of Python3 online submissions for Range Sum Query 2D - Immutable.
Memory Usage: 24.9 MB, less than 54.96% of Python3 online submissions for Range Sum Query 2D - Immutable."""