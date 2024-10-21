# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
       # Initialize stack with root node and corresponding visit flag
        stack = [root]
        visit = [False]  # False means first visit, True means process node
        res = []  # Store result of postorder traversal
       
        while stack:
           # Get current node and its visit status
            cur, v = stack.pop(), visit.pop()
           
            if cur:  # If node exists
                if v:  # If already visited before
                   # Process node by adding to result
                   # This happens after both children are processed
                    res.append(cur.val)
                else:
                   # First time visiting this node
                   # Add nodes in reverse order of postorder traversal
                   # Because stack is LIFO (Last In First Out)
                   
                   # Add current node again with visit=True
                   # This will be processed after both children
                    stack.append(cur)
                    visit.append(True)
                   
                   # Add right child first (will be processed second)
                    stack.append(cur.right)
                    visit.append(False)
                   
                   # Add left child last (will be processed first)
                    stack.append(cur.left)
                    visit.append(False)
                   
        return res