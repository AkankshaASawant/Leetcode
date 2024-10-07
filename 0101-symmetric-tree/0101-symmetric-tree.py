# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        # Initialize roots as left and right 
        def same(left, right): 
            
            # If both the roots are NULL = True
            if not left and not right: 
                return True
            
            # IT one is NULL and other is NOT NULL = False
            if not left or not right: 
                return False
            
            # If the values are same and both left and right 
            # sub root of the main root are same then = True
            return (left.val == right.val and 
               same(left.left, right.right) and 
               same(left.right, right.left))
        
        # Call function with roots
        return same(root.left, root.right)