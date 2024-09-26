# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        # if the root is Null, return None
        if not root: 
            return None         
        
        # Swap the children of the current root node
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        # Recursively invert the left & right subtree
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # Return root of the inverted tree
        return root