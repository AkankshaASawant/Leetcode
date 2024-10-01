class Solution(object):
    def removeElement(self, nums, val):
        # Initialize k pointer from 0th position
        k = 0
        
        # Iterate through the entire array
        for i in range(len(nums)): 
            # If the current num is != value we want to remove
            if nums[i] != val: 
                # Move this element to position at which k pointer is present 
                nums[k] = nums[i]
                # Increase k to find next non-val element
                k += 1
        
        # Return count of non-val numbers
        return k
        