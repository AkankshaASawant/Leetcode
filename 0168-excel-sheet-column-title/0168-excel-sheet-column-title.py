class Solution(object):
    def convertToTitle(self, columnNumber):
        # Initialize empty string to store result
        res = "" 
        
        while columnNumber > 0:
            # Subtract 1 from columnNumber because Excel column titles are 1-based
            # Use modulo 26 to get remainder (0-25) corresponding to A-Z
            offset = (columnNumber - 1) % 26
            
            # Convert offset to corresponding letter (A-Z)
            # ord('A') gives ASCII value of 'A'
            # Adding offset gives desired letter
            res += chr(ord('A') + offset) 
            
            # Integer divide by 26 to move to next digit
            # Subtract 1 first because of 1-based indexing
            columnNumber = (columnNumber - 1) // 26 
             
        # Reverse the string since we built it from right to left
        return res[::-1]
