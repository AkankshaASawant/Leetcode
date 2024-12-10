class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Initialize the result with the length of the array
        # This is because the array is expected to have numbers from 0 to n
        res = len(nums)
        
        for i in range(len(nums)): 
            # Use the mathematical trick of XOR-like cancellation
            # Add the current index and subtract the current array value
            # This helps identify the missing number by balancing out the existing numbers
            res += (i - nums[i])
        
        # Return the final calculated number, which will be the missing number
        return res