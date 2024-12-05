class MyQueue:
    def __init__(self):
        # Initialize two stacks: s1 for pushing elements, s2 for popping
        self.s1 = []  # Incoming stack
        self.s2 = []  # Outgoing stack
    
    def push(self, x: int) -> None:
        # Always push new elements to s1 (incoming stack)
        self.s1.append(x)
    
    def pop(self) -> int:
        # If outgoing stack is empty, transfer elements from incoming stack
        if not self.s2: 
            # Move all elements from s1 to s2, reversing their order
            while self.s1: 
                self.s2.append(self.s1.pop())
        
        # Remove and return the top element from outgoing stack
        return self.s2.pop()
            
    def peek(self) -> int:
        # Similar to pop(), but without removing the element
        # If outgoing stack is empty, transfer elements from incoming stack
        if not self.s2: 
            while self.s1: 
                self.s2.append(self.s1.pop())
        
        # Return the top element of outgoing stack without removing it
        return self.s2[-1]
    
    def empty(self) -> bool:
        # Queue is empty if both stacks have no elements
        return max(len(self.s1), len(self.s2)) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()