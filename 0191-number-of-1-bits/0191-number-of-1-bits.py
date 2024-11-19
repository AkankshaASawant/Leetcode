class Solution:
    def hammingWeight(self, n: int) -> int:
        # Initialize a counter to track the number of 1 bits
        res = 0
        
        # Solution 1: Brian Kernighan's Algorithm - Efficiently counts set bits
        # n &= (n - 1) removes the least significant 1-bit
        while n: 
            n &= (n - 1)
            res += 1
        return res
    
        # Solution 2: Bit Manipulation using Modulo and Right Shift
        # Iterate until n becomes 0
        # Add 1 if bit is 1, otherwise 0
        # Right shift bits to check next bit
        # Equivalent to integer division by 2
        while n: 
            res += n % 2
            n = n >> 1
        return res