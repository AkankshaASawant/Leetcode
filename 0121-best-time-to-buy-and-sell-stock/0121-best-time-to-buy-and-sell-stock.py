class Solution(object):
    def maxProfit(self, prices): 
        l, r = 0, 1 # inintial places
        maxP = 0    # initially it should be 0
        
        while r < len(prices): 
            # To check if it is profitable or not
            if prices[r] > prices[l]: 
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else: 
                l = r  # Move l to righttill it has the smallest value
            r += 1     # For r try all values from first value
            
        return maxP     
        