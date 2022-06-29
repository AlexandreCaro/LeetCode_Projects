import numpy as np

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        valid_list = list()
        
        distance_list = [0]
        
        n,m = len(nums1), len(nums2)
        
        distance_reverse = list()
        
        for i in range(n):
            
            for j in range(m-1, 0, -1):
                
                if i<=j and nums1[i]<=nums2[j]:
                    
                    distance_reverse.append(np.abs(j-i))
                    
                    break
                    
        if len(distance_reverse)==0:
            
            return 0
                    
        return np.max(distance_reverse)
        
        if max(n, m)<=5:
            
            for i in range(n):
            
                for j in range(m):
                
                 if i<=j and nums1[i]<=nums2[j]:
                    
                     distance = np.abs(j-i)
                    
                     maximum = np.max(distance_list)
                    
                     if distance > maximum:
                        
                         distance_list.append(distance)
                            
            return np.max(distance_list)

        elif max(n,m)>5:
            
            start_i, end_i = 0, n-1
            
            while start_i<=end_i:

                middle_i = (start_i+end_i)//2

                start_j, end_j = middle_i, m-1

                while start_j<=end_j:

                    middle_j = (start_j+end_j)//2

                    if middle_i<=middle_j and nums1[middle_i]<=nums2[middle_j]:

                        distance = np.abs(middle_j-middle_i)

                        maximum = np.max(distance_list)

                        if distance > maximum:

                            distance_list.append(distance)

                        start_ = middle_j+1

                    elif nums1[middle_i]>nums2[middle_j]:

                        end_j = middle_j-1

                if nums1[middle_i]<= nums2[middle_j]:

                    end_i = middle_i-1

                elif nums1[middle_i]>nums2[middle_j]:

                    start_i = middle_i+1
                        
                
            
#             for j in range(m):
                
#                 if i<=j and nums1[i]<=nums2[j]:
                    
#                     distance = np.abs(j-i)
                    
#                     maximum = np.max(distance_list)
                    
#                     if distance > maximum:
                        
#                         distance_list.append(distance) 

                    
        #print(valid_list)
        
        #print(distance_list)
        
        distance_reverse = list()
        
        for i in range(n):
            
            for j in range(m, 1, -1):
                
                if i<=j and nums1[i]<=nums2[j]:
                    
                    distance_reverse.append(np.abs(j-i))
                    
                    break
                    
        return np.max(distance_reverse)
        
        if len(distance_list)==1:
            
            return 0
                    
        return np.max(distance_list)
    
"""You are given two non-increasing 0-indexed integer arrays nums1​​​​​​ and nums2​​​​​​.

A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, is valid if both i <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i​​​​.

Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.

An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length.

 

Example 1:

Input: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
Output: 2
Explanation: The valid pairs are (0,0), (2,2), (2,3), (2,4), (3,3), (3,4), and (4,4).
The maximum distance is 2 with pair (2,4).
Example 2:

Input: nums1 = [2,2,2], nums2 = [10,10,1]
Output: 1
Explanation: The valid pairs are (0,0), (0,1), and (1,1).
The maximum distance is 1 with pair (0,1).
Example 3:

Input: nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
Output: 2
Explanation: The valid pairs are (2,2), (2,3), (2,4), (3,3), and (3,4).
The maximum distance is 2 with pair (2,4).
 

Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[j] <= 105
Both nums1 and nums2 are non-increasing."""