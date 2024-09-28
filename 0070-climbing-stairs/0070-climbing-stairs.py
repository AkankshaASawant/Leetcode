class Solution(object):
    def climbStairs(self, n):
        # Initialize variables for 1 and 2 steps
        one, two = 1, 1      
        
        # n-1 because we've already set up base cases
        for n in range(n - 1): 
            tmp = one         # Store one value before updating
            one = one + two   # number of ways to reach current step
            two = tmp         # This sets up for the next iteration
        return one            # one contains number of ways to climb n stairs