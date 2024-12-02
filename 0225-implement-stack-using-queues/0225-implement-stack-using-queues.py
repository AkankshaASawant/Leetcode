from collections import deque

class MyStack:
    def __init__(self):
        # Initialize empty queue to simulate stack
        self.q = deque()
    
    def push(self, x: int) -> None:
        # Add element to the end of queue
        self.q.append(x)
    
    def pop(self) -> int:
        # Rotate queue to bring top element to front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        
        # Remove and return the top element
        return self.q.popleft()
    
    def top(self) -> int:
        # Rotate queue to bring top element to front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        
        # Get top element
        top = self.q[0]
        
        # Rotate back to original order
        self.q.append(self.q.popleft())
        
        return top
    
    def empty(self) -> bool:
        # Check if queue is empty
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()