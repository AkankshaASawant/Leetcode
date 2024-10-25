from string import ascii_uppercase as asc

class Solution(object):
    def titleToNumber(self, columnTitle):
        # Create a dictionary mapping uppercase letters to their position (1-26)
        d = {asc[i]:i+1 for i in range(len(asc))}
        
        # Reverse the input string to process from right to left
        s = columnTitle[::-1]
        
        # Initialize the result counter
        count = 0
        
        # Iterate through each character with its position
        # Similar to decimal system but with base 26
        for i, j in enumerate(s): 
            count += d[j]*(26**i)
            
        return count