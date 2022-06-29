import math

class Solution:
    def twoSum(self, numbers, target):
        
        list_index = list()
        
        n = len(numbers)
        
        max_iter = math.log2(n)
        
        somme = 0
        
        if n>6:
            
            for i in range(n):
                
                somme = numbers[i]
                
                if somme+numbers[-1]<target:
                    
                    continue
                    
                elif somme + numbers[-1] == target:
                    
                    list_index.extend([i+1, n])
                    
                    return list_index
                
                elif somme + numbers[-1]>target:
                    
                    j = 1
                    
                    index = 1
                    
                    while j<max_iter:
                        
                        somme = numbers[i]
                        
                        somme += numbers[index]
                        
                        if somme< target:
                            
                            index = min(index + n//(2**j), n-1)
                            
                        elif somme>target:
                            
                            index = max(index - n//(2**j),0)
                            
                        elif somme==target:
                            
                            list_index.extend([i+1, index+1])
                            
                            return list_index
                        
                        j+=1
                        
                        print(index)
                        
                    count = 1
                
                    while count<5:
                    
                        somme = numbers[i]
                        
                        if i!=index:
                    
                            if somme+numbers[index]<target:

                                index = min(index+1, n-1)

                            elif somme+numbers[index]==target:

                                print("Got it!")

                                list_index.extend([i+1, index+1])
                                
                                list_index.sort()

                                return list_index

                            elif somme+numbers[index]>target:

                                index = max(index-1,0)
                                
                        else:
                            
                            pass

                        count+=1
        
        else:

        
            for i in range(n):

                somme = numbers[i]

                #print(somme)

                if i<n-1:

                    for j in range(i+1, n):

                        somme = numbers[i]

                        somme+=numbers[j]

                        #print("after",somme)

                        if somme==target:

                            list_index.extend([i+1, j+1])

                            return list_index

                elif i==n-1:

                    continue
                    
        return list_index
    
"""Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution."""