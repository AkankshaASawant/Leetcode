class Solution:
    def addDigits(self, num: int) -> int:
        # If the num is 0 then return 0
        if num == 0: 
            return 0
        
        # Digital root calculation 
        if num % 9 == 0: 
            return 9
        else: 
            return num % 9