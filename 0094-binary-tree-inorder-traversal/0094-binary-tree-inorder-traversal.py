# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        # Initialize result list to store the inorder traversal
        res = []
        # Initialize stack for iterative traversal
        stack = []
        # Start with the root node
        cur = root
        
        # Continue traversal while there are nodes to process
        while cur or stack:
            # Traverse to the leftmost node, pushing all nodes onto the stack
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # Process the current node
            cur = stack.pop()  # Pop the last node pushed (leftmost unprocessed node)
            res.append(cur.val)  # Add its value to the result
            
            # Move to the right child
            cur = cur.right
        
        # Return the final inorder traversal
        return res

    # The commented-out code below is a recursive implementation of inorder traversal
    #     def inorder(root): 
    #         if not root: 
    #             return
    #         inorder(root.left)
    #         res.append(root.val)  
    #         inorder(root.right)
            
    #     inorder(root)  
    #     return res