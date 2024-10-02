class Solution(object):
    def lengthOfLastWord(self, s):
        i = len(s)           # Length of the string
        w = 0                # Initial length of word 
        
        while i > 0:         # Start from end of the string
            i -= 1           # Move to the previous char
            if s[i] != " ":  # If it is not space 
                w += 1       # Increase length of word 
            elif w > 0:      # If space come it will again start counting it
                return w     # Return the length of the last word
        
        return w           # final length of word
        
        