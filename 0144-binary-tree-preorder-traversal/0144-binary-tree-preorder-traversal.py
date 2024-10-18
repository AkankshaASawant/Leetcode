# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        # Initialize loop from current root node and take stack as empty list
        cur, stack = root, [] 
        # Initialize result from empty list
        res = []
        
        # Loop is until the current pointer or stack is not null
        while cur or stack: 
            if cur:                     # If current pointer is not null
                res.append(cur.val)     # Then add root value to result
                stack.append(cur.right) # And add left root value to stack
                cur = cur.left          # As take current value from left root first
                
            else:                       # If current pointer is null (from left)
                cur = stack.pop()       # Take values from stack
                
        return res                      # Return the result list
                