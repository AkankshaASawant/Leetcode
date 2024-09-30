class Solution(object):
    def longestCommonPrefix(self, strs):
        # empty string to store the common prefix
        result = ""
        
        # Iterate through each character position in the first string
        for i in range(len(strs[0])): 
            
            # For each string in the list of strings
            for s in strs: 
                
                # If we've reached the end of the current string
                # or the character at position i doesn't match the first string
                if i == len(s) or s[i] != strs[0][i]: 
                    
                    # We've found the end of the common prefix, so return it
                    return result
            
            # If we've made it here, the character is common to all strings
            # so add it to our result
            result += strs[0][i]
        
        # If we've made it through all characters, 
        # the entire first string is the common prefix
        return result 
                