class Solution(object):
    def singleNumber(self, nums):
        # Use XOR Algorithm 
        # XOR has the property: a ^ a = 0 and a ^ 0 = a
        
        # Initialize the result variable to 0
        result = 0
        
        # Iterate through each number in the input list
        for i in nums:          # i = current num
            
            # XOR the current number with the result
            # Duplicate numbers will cancel out, leaving only the single number
            result = i ^ result 
            
        # Return the single number 
        return result
        