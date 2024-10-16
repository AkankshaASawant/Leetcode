class Solution(object):
    def isPalindrome(self, x): 
        # If the number is negative, it's not a palindrome
        if x < 0: 
            return False
        
        # If number is 0, it's a palindrome
        if x == 0:
            return True
            
        # Find the appropriate divisor to get the leftmost digit
        div = 1
        temp = x
        while temp >= 10:
            div *= 10
            temp //= 10
            
        while x:
            right = x % 10  # Get rightmost digit
            left = x // div  # Get leftmost digit
            
            # Compare the leftmost and rightmost digits
            if left != right:
                return False
            
            # Remove the leftmost and rightmost digits
            x = (x % div) // 10
            div = div // 100
        
        return True
                