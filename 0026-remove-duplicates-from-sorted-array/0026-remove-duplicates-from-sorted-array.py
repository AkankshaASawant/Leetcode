class Solution(object):
    def removeDuplicates(self, nums):
        # Initialize l and r pointers from 1st position
        l = 1
        
        # Iterate through the array starting from the second element
        for r in range(1, len(nums)): 
            # If current num is not equal to previous num 
            if nums[r] != nums[r - 1]: 
                # then num on r pointer will com to l pointer position. 
                nums[l] = nums[r]
                # and l pointer will take the next position
                l += 1
        
        # To know how many repeated nums are there
        return l
        