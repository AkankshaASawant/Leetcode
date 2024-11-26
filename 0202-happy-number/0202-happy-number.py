class Solution:
    def isHappy(self, n: int) -> bool:
        # Create a set to track numbers we've already seen
        visited = set()
        
        # Continue until we either find a happy number or detect a cycle
        while n not in visited:
            # Add the current number to our visited set
            visited.add(n)
            
            # Calculate the sum of squared digits
            # Convert number to string to easily iterate through digits
            # Square each digit and sum the results
            n = sum(int(digit) ** 2 for digit in str(n))
            
            # If we reach 1, it's a happy number
            if n == 1:
                return True
        
        # If we exit the loop without finding 1, it means we've found a cycle
        # Therefore, it's not a happy number
        return False