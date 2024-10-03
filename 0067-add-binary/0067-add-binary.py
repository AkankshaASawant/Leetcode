class Solution(object):
    def addBinary(self, a, b):
        result = ""
        carry = 0
        
        a, b = a[::-1], b[::-1]          # Reverse both strings
        
        # Iterate through string with max length 
        for i in range(max(len(a), len(b))): 
            
            # Get digit from string, or 0 if we've reached the end of the string
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0 
            
            # Sum the digits and the carry
            total = digitA + digitB + carry
            # The current bit is the remainder when divided by 2
            char = str(total % 2)
            # Add the new bit to the left of the result string
            result = char + result
            # Update carry for the next iteration
            carry = total // 2
            
        # If there's still a carry after the loop, add it to the result
        if carry: 
            result = "1" + result 
        return result