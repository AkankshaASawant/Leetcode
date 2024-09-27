# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        
        if not p and not q:  # Both nodes are None, the trees are identical
            return True
        
        # If one node is None and the other isn't, or if the values don't match,
        # the trees are not identical
        if not p or not q or p.val != q.val: 
            return False
        
        # Recursively check if the left subtrees and right subtrees are identical
        return (self.isSameTree(p.left, q.left) and
               self.isSameTree(p.right, q.right))