class Solution(object):
    def romanToInt(self, s):
        # Largest before Smallest = Add them
        # Smallest before Largest = Subtract them
        
        # Dictionary mapping Roman numeral symbols to their integer values
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        result = 0 
        s = s.upper()  # Convert input to uppercase
        
        # Iterate through each character in the input string
        for i in range(len(s)): 
            # Check if there's a next character and if current value is less than the next
            if i + 1 < len(s) and roman.get(s[i], 0) < roman.get(s[i + 1], 0): 
                # subtract the current value
                result -= roman.get(s[i], 0)
            else: 
                # add the current value
                result += roman.get(s[i], 0)
        
        return result