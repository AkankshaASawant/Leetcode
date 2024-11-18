class Solution:
    def reverseBits(self, n: int) -> int:
        # Initialize result variable to store the reversed bits
        res = 0
        
        # Iterate through all 32 bits of the input integer
        for i in range(32): 
            # Extract the i-th bit from the input number
            # Right shift n by i positions and use bitwise AND with 1 to get the bit
            bit = (n >> i) & 1
            
            # Place the extracted bit in the reversed position
            # Left shift the bit to (31 - i) position and 
            # use bitwise OR to set it in result
            res = res | (bit << (31 - i))
        
        # Return the integer with its bits reversed
        return res