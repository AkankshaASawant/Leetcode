class Solution(object):
    def minCostClimbingStairs(self, cost):
        # Add a 0 at the end of the cost list
        cost.append(0)
        
        # Iterate backwards through the list, 
        # starting from the third-last element
        for i in range(len(cost) -3, -1, -1): 
            
            # For each step, add the minimum cost of taking 
            # either one or two steps forward
            cost[i] += min(cost[i + 1], cost[i + 2])
            
        # The minimum cost to reach the top is 
        # the minimum of starting from the first or second step    
        return min(cost[0], cost[1])