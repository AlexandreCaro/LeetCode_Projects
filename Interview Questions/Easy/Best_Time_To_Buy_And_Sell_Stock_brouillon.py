import numpy as np

class Solution:
    def maxProfit(self, prices):
        
        if len(prices)==0:
            
            return 0
        
        n = len(prices)
        
        stock_min, index_min = np.min(prices), np.argmin(prices)
        
        stock_max, index_max = np.max(prices), np.argmax(prices)
        
        dis_min, dis_max = index_min, n-1-index_max
        
        print(stock_min, stock_max)
        
        print("dis", dis_min, dis_max)
        
        if index_min < index_max:
            
            return stock_max-stock_min
        
        if index_max<index_min and dis_max>=dis_min:
            
            prices.pop(index_max)
            
            return self.maxProfit(prices)
        
        elif index_min>index_max and dis_min>=dis_max:
            
            prices.pop(index_min)
            
            return self.maxProfit(prices)
        
        else:
            
            return stock_max-stock_min

"""
class Solution:
    def maxProfit(self, prices):
        
        profit = 0
        
        stock = prices[0]
        
        for index, price in enumerate(prices):
            
            if index==len(prices)-1:
                
                break
            
#             j = index+1
            
#             while price < prices[j]:
                
#                 j+=1
            
            if prices[index+1]<price:
                
                stock = 0
                
            elif prices[index+1]>price:
                
                stock = prices[index+1]
                
                profit += prices[index+1]-price
                
        return profit
    """
    
    