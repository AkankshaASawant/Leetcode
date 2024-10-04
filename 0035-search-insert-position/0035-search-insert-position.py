class Solution(object):
    def searchInsert(self, nums, target):
        l , r = 0, len(nums) - 1        # Initialize two pointers
        
        while l <= r: 
            mid = (l + r) // 2          # middle index
            
            if target == nums[mid]:     # If the target is at middle return it as it is
                return mid
            
            if target > nums[mid]:      # If the target is greater than middle num
                l = mid + 1             # search in the right half of the array
            else: 
                r = mid - 1             # search in the right half of the array
        
        # If the target is not found, return the left pointer
        # Insert target to maintain the sorted order
        return l