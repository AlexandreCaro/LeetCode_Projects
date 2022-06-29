class Solution:
    d_hash = {}
	# Numbers of Ways to reach step 1
    d_hash[1] =  1
	# Numbers of Ways to reach step 2
	#1+1,2
    d_hash[2] = 2
    def climbStairs(self, n: int) -> int:
        if n in self.d_hash:
            return self.d_hash[n]
        self.d_hash[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.d_hash[n]
    
"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step"""