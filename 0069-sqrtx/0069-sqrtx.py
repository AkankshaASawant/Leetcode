class Solution(object):
    def mySqrt(self, x):
        # Initialize binary search boundaries
        # l = lower bound, from 0
        # r = upper bound, from input x
        l, r = 0, x
        # res will store the floor value of square root
        res = 0
        
        while l <= r:
            # Calculate middle point
            m = l + ((r - l) // 2)
            
            # If m**2 > x then search in the lower half
            if m**2 > x:
                r = m - 1
                
            # If m**2 < x then, search in the upper half
            # and store current m as potential result
            elif m**2 < x:
                l = m + 1
                res = m
                
            # If  m**2 = x exact square root
            else:
                return m
                
        # Return the floor value of square root
        return res