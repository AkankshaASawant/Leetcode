# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # Base case: if root is None, return empty list
        if not root:
            return []
        
        # If it's a leaf node, return its value as a single-element list
        if not root.left and not root.right:
            return [str(root.val)]
        
        # Initialize list to store all paths
        paths = []
        
        # Recursively get paths from left subtree
        if root.left:
            for path in self.binaryTreePaths(root.left):
                paths.append(str(root.val) + '->' + path)
        
        # Recursively get paths from right subtree
        if root.right:
            for path in self.binaryTreePaths(root.right):
                paths.append(str(root.val) + '->' + path)
        
        # Return all paths from this node
        return paths