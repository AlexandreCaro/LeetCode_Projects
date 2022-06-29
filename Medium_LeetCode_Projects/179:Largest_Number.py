class Solution_br:
    def largestNumber(self, nums) -> str:
        
        nums = sorted(nums, key= lambda t:str(t)[0])
        
        print(nums)
        
        string = ""
        
        for i in nums[:]:
            
            string += str(nums[-1])
            
            nums.pop()
        
        return string
        
#         filtered_10 = list(filter(lambda scores: scores <10, nums))
#         filtered_100 = list(filter(lambda scores: 10 <= scores and scores <100, nums))
        
#         string = ""
        
#         for i in filtered_10[:]:
            
#             string += str(filtered_10[-1])
            
#             filtered_10.pop()
            
#         for i in filtered_100[:]:
            
#             string += str(filtered_100[-1])
            
#             filtered_100.pop()
            
#         return string

from functools import cmp_to_key
            
class Solution:
    def largestNumber(self, nums) -> str:
        
        if (all(v==0 for v in nums)):
            
            return "0"
        
        res = sorted(nums, key= cmp_to_key(lambda i, j: -1 if str(j) + str(i) < str(i) + str(j) else 1))
        
        string = "".join([str(i) for i in res])
        
        return string
    
"""Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109"""

"""Runtime: 85 ms, faster than 20.17% of Python3 online submissions for Largest Number.
Memory Usage: 14 MB, less than 24.40% of Python3 online submissions for Largest Number."""

"Solution"

class LargerNumKey(str):
    
    def __lt__(x, y):
        
        return x+y > y + x
    
class Solution_cor:
    
    def largestNumber(self, nums):
        largest_num = "".join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num