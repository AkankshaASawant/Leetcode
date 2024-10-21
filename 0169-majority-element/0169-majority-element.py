class Solution(object): 
    def majorityElement(self, nums):
       # Initialize result to majority element
       # Initialize count to keep track
        res, count = 0, 0
       
       # Iterate through each number
        for n in nums:
            
            # If count becomes 0, update res to current number
            if count == 0:
                res = n
               
            # If current number matches res, increment count Otherwise decrement
            count += (1 if n == res else -1)
           
        # Return the majority element
        return res