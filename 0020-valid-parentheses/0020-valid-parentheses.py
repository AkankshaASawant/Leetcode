class Solution(object):
    def isValid(self, s): 
        # To keep track of opening brackets
        stack = [] 
        closeToOpen = {')': '(', ']': '[', '}': '{'} 
        
        for c in s: 
            if c in closeToOpen: 
                # If the stack is not empty and the top of the stack is the
                # opening bracket that matches the current closing bracket
                if stack and stack[-1] == closeToOpen[c]: 
                    # Pop the top of the stack (the matching opening bracket)
                    stack.pop()
                else: 
                    return False
            else: 
                # If the current character is not a bracket, push it onto the stack
                stack.append(c)
                
        return True if not stack else False        
        