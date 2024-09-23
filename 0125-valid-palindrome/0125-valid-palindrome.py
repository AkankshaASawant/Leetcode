class Solution(object):
    def isPalindrome(self, s):
        '''A palindrome is a word, phrase, number, or sequence 
           that reads the same backward as forward.
           Examples: r_a_c_e_c_a_r'''
        
        l, r = 0, len(s) - 1 # initialize left and right pointers
        
        while l < r: 
            while l < r and not self.alphaNum(s[l]): #If l is not alphaNum skip the char
                l += 1
            while r > l and not self.alphaNum(s[r]): # Same for r and move ahead 
                r -= 1
            if s[l].lower() != s[r].lower(): #if l & r are not the same chars 
                return False
            l, r = l + 1, r - 1 
        return True
   
    # create a function for ASCII characters
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))