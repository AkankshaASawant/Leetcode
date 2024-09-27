# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        # If subRoot is None, it's considered a subtree of any tree
        if not subRoot: 
            return True
        
        # If root is None but subRoot isn't, subRoot can't be a subtree
        if not root: 
            return False

        # Check if the current root and subRoot are identical trees
        if self.SameTree(root, subRoot):
            return True
        
        # If not, recursively check left and right subtrees
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))

    def SameTree(self, root, subRoot):
        # If both trees are empty, they're the same
        if not root and not subRoot:
            return True
        
        # If both nodes exist and have the same value, recursively check their subtrees
        if root and subRoot and root.val == subRoot.val:
            return (self.SameTree(root.left, subRoot.left) and 
                    self.SameTree(root.right, subRoot.right))
        
        # If we reach here, the trees are different
        return False