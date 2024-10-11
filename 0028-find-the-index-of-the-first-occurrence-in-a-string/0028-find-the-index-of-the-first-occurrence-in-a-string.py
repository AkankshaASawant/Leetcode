class Solution(object):
    def strStr(self, haystack, needle):
        # Edge case: if needle is empty, return 0
        if needle == "": 
            return 0
        
        # Iterate through haystack, but only up to the point where needle could still fit
        for i in range(len(haystack) + 1 - len(needle)): 
            # The following commented-out code is an alternative implementation
            # It checks each character of the needle against the haystack
            # #     for j in range(len(needle)): 
            # #         if haystack[i + j] != needle[j]:
            # #             break 
            # #         if j == len(needle) - 1: 
            # #             return i
                
            # Check if the substring of haystack matches the needle
            # This is a more concise way to check for a match compared to 
            # the commented-out code above
            if haystack[i : i + len(needle)] == needle: 
                return i  # If a match is found, return the starting index
        
        # If no match is found after checking all possible positions, return -1
        return -1