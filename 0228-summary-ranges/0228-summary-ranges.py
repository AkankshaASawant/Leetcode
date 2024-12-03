class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]: 
        # Initialize result list to store range summaries
        ans = []
        i = 0
        
        # Iterate through the entire input list
        while i < len(nums): 
            # Mark the start of current range
            start = nums[i]
            
            # Find the consecutive sequence's end
            while i < len(nums) - 1 and nums[i] + 1 == nums[i+1]: 
                i += 1
                
            # Check if range spans multiple numbers
            if start != nums[i]: 
                # Create range string with start and end
                ans.append(str(start) + '->' + str(nums[i]))
            else:
                # Single number range
                ans.append(str(nums[i]))
                
            # Move to next potential range
            i += 1
                
        return ans