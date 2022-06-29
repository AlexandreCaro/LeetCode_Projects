"""Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

"""

import math

class Solution:
    def peakIndexInMountainArray(self, arr):
        
        n = len(arr)//2
        
        if arr[n]>arr[n-1] and arr[n]>arr[n+1]:
            
            return n
        
        elif arr[n]> arr[n-1] and arr[n]<arr[n+1]:
            
            n = n + n//2
            
        elif arr[n]<arr[n-1] and arr[n]>arr[n+1]:
            
            n = n - n//2
            
        max_iter = math.log2(len(arr))
        
        j=0
        
        while j<max_iter:
            
            if n==0:
                
                if arr[0]>arr[1]:
                    
                    return 0
                
                else:
                    
                    n+=1
                    
                    continue
                    
            if n==len(arr)-1:
                
                if arr[n]>arr[n-1]:
                    
                    return n
                
                else:
                    
                    n-=1
                    
                    continue
                    
            if n==len(arr):
                
                n-=2
                
            if n>len(arr):
                
                n=len(arr)-2
            
            if arr[n]>arr[n-1] and arr[n]>arr[n+1]:
            
                return n
        
            elif arr[n]> arr[n-1] and arr[n]<arr[n+1]:
            
                n = min(n + n//(2**j), len(arr)-1)
            
            elif arr[n]<arr[n-1] and arr[n]>arr[n+1]:
            
                n = max(0,n - n//(2**j))
            
            j+=1
            
        while True:
            
            if arr[n]>arr[n-1] and arr[n]>arr[n+1]:
                
                break
                
            elif arr[n]>arr[n-1] and arr[n]<arr[n+1]:
                
                n += 1
                
            elif arr[n]<arr[n-1] and arr[n]>arr[n+1]:
                
                n-=1
            
        return n
    
s1 = [0,1,0]
s2 = [0,2,1,0]
s3 = [0,10,5,2]
s4 = [12,13,19,41,55,69,70,71,96,72]
s5 = [19,24,25,29,34,39,50,51,56,61,67,82,87,88,97,73,72,23]
s6 = [40370,45032,51739,64126,115331,124874,127869,137108,142665,149607,160239,169054,171077,192890,194555,211837,217366,228416,231510,267051,289309,292546,314437,338983,349498,369838,392855,397872,398130,402115,413358,424366,431047,446976,453541,462092,471879,481179,481539,511285,548436,558359,573523,586071,595562,607009,619886,644930,646689,672143,716225,721626,727026,736895,755018,759060,770233,777456,780746,783606,785850,829164,832455,846854,851797,856851,863727,870611,883664,889018,906155,926011,931219,939022,944807,950814,952362,954245,982179,992336,998673,911666,904518,767586,761411,736299,665603,559601,423488,378586,332153,276627,260384,208757,106222,90331,73093,54013,46440,10960]
