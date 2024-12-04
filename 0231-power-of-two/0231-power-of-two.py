class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Solution type 1: Iterative Doubling
        # Continuously multiply 1 by 2 until reaching or exceeding n
        # If exactly equal, n is a power of 2
        ''' x = 1
            while x < n: 
                x *= 2
            return x == n '''
        
        # Solution type 2: Bitwise AND Operation
        # A power of 2 has only one bit set
        # Subtracting 1 flips all bits below the set bit
        # AND operation with (n-1) will be 0 only for powers of 2
        # return n > 0 and (n & (n - 1)) == 0
        
        # Solution type 3: Modulo Bit Manipulation
        # Uses the maximum power of 2 within 32-bit integer range
        # Checks if 2^30 is divisible by n
        return n > 0 and ((1 << 30) % n) == 0