import numpy as np

class Solution:
    def maxArea(self, height) -> int:
        
        matrix = np.zeros((len(height), len(height)))
        
        for i in range(len(height)):
            
            for j in range(len(height)):
                
                matrix[i][j] = min(height[i], height[j])*(abs(i-j))
        
        return int(matrix.max())

class Solution_corr:
    def maxArea(self, height) -> int:
        
        l, r = 0, len(height)-1
        
        res = 0
        
        while l < r :
            
            res = max(res, (r-l)*min(height[l], height[r]))
            
            if height[l]<height[r]:
                
                l += 1
                
            else:
                
                r-= 1
                
        return res
    
"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104"""

"""Runtime: 1431 ms, faster than 7.17% of Python3 online submissions for Container With Most Water.
Memory Usage: 45.1 MB, less than 17.16% of Python3 online submissions for Container With Most Water."""