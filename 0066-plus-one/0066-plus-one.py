class Solution(object):
    def plusOne(self, digits):
        
        digits = digits[::-1]       # Reverse the digit array
        one, i = 1, 0               # Initialize the carry one and the index of current digit 
        
        while one:                  # If there is carry one
            if i < len(digits):     # if we are in bound
                if digits[i] == 9:  
                    digits[i] = 0   # If last digit is 9 maze it 0
                else: 
                    digits[i] += 1  # If not 9 add 1
                    one = 0         # with no carry one
                    
            else: 
                digits.append(1)    # if we've gone through all digits, append 1
                one = 0             # Set carry to 0
            i += 1
        
        return digits[::-1]         # Return the reversed list back to original order
                    