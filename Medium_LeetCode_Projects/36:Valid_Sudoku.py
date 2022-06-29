"358/507 Test cases passed."

class Solution:
    def isValidSudoku(self, board) -> bool:
        
        n = len(board)
        
        for i in range(n):
            
            for j in range(n):
                
                if board[i][j].isdigit():
                    
                    if board[i].count(board[i][j])>1:
                        
                        return False
                    
                    if board[:][j].count(board[i][j])>1:
                        
                        return False
                    
                    if board[i//3:min(i//3+i%3,n-1)][j//3:min(j//3+j%3,n-1)].count(board[i][j])>1:
                        
                        return False
            
        return True
                    
"Maintenant"

class Solution_br:
    def isValidSudoku(self, board) -> bool:
        
        n = len(board)
        
        for i in range(n):
            
            for j in range(n):
                
                print(board[i//3:min(i//3+3,n-1)][j//3:min(j//3+3,n-1)])
                
                if board[i][j].isdigit():
                    
                    if board[i].count(board[i][j])>1:
                        
                        return False
                    
                    if board[:][j].count(board[i][j])>1:
                        
                        return False
                    
                    submatrix = [board[a][b] for a in range(i//3, min(i//3+3,n-1)) for b in range(j//3, min(j//3+3, n-1))]
                    
                    if submatrix.count(board[i][j])>1:
                        
                        return False
                    
        
        return True
    
"422/507 Test cases:"

class Solution2:
    def isValidSudoku(self, board) -> bool:
        
        n = len(board)
        
        for i in range(n):
            
            for j in range(n):
         
                if board[i][j].isdigit():
                    
                    if board[i].count(board[i][j])>1:
                        
                        return False
                    
                    if board[:][j].count(board[i][j])>1:
                        
                        return False
                    
                    for a in range(3*(i//3), 3*(i//3+1)):
                        
                        for b in range(3*(j//3), 3*(j//3+1)):
                            
                            if a != i and b != j:
                                
                                if board[a][b]==board[i][j]:
                                    
                                    print(a, b, i, j, board[a][b])
                                    
                                    return False    
        
        return True
                    