"""We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked."""

# The guess API is already defined for you.
#@param num, your guess
#@return -1 if num is higher than the picked number
#         1 if num is lower than the picked number
#         otherwise return 0
#def guess(num: int) -> int:

"""Il va falloir calculer a priori le nombre maximal de divisions par 2 qu'il faudra faire
et ce sera égal à np.log(n)."""

import math

class Solution:
    
    def guessNumber(self, n: int) -> int:
        
        num=n//2
        
        count=1
        
        max_iter = int(math.log2(n))
        
        my_guess=guess(num)
        
        while count<max_iter:
            
            if my_guess==1:
            
                num+=n//(2**count)
                
            elif my_guess==-1:
            
                num-= n//(2**count)
                
            elif my_guess==0:
                
                break
                
            my_guess = guess(num)
            
            count+=1
            
        while guess!=0:
            
            if my_guess==1:
                
                num+=1
                
            elif my_guess==-1:
                
                num-=1
                
            elif my_guess==0:
                
                return num
            
            my_guess = guess(num)
            
        return num