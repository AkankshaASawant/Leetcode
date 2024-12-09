class Solution:
    def isUgly(self, n: int) -> bool:
        # Return False for non-positive numbers
        if n <= 0: 
            return False
        
        # Try dividing by prime factors 2, 3, and 5
        for p in [2, 3, 5]: 
            # Continue dividing while the number is divisible by the current prime
            while n % p == 0: 
                # Update n by integer division
                n = n // p
        
        # If n reduces to 1, it's an ugly number
        return n == 1