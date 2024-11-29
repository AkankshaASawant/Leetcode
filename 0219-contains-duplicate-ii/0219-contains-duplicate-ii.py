class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Create a sliding window set to track unique elements
        window = set()
        
        # Initialize the left pointer of the sliding window
        L = 0
        
        # Iterate through the array using the right pointer
        for R in range(len(nums)): 
            # If window size exceeds k, remove the leftmost element
            # This maintains a window of maximum size k
            if R - L > k: 
                window.remove(nums[L])
                L += 1
            
            # Check if current element is already in the window
            # If true, we've found duplicate within k distance
            if nums[R] in window: 
                return True
            
            # Add current element to the window
            window.add(nums[R])
        
        # No duplicates found within k distance
        return False