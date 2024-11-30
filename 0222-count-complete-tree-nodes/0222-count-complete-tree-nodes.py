# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Base case: empty tree
        if not root: return 0
        
        # Calculate left and right subtree heights
        def height(node, is_left):
            h = 0
            while node:
                h += 1
                node = node.left if is_left else node.right
            return h
        
        # Get left and right heights
        l, r = height(root, True), height(root, False)
        
        # If perfect binary tree, return total nodes
        if l == r:
            return (1 << l) - 1
        
        # Recursively count nodes in left and right subtrees
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)