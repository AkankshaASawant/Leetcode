# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        if not root: 
             return 0
        # return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        
        # Initialize an empty list to store nodes and their depths
        level = []

        # Start with depth 1 for the root
        depth = 1

        # Add the root node and its depth to the level list
        level.append((root, depth))

        # Begin BFS traversal
        while level:
            # Remove and get the first node and its depth from the list
            cur, d = level.pop(0)

            # If current node is a leaf (no children), return its depth
            if cur.left is None and cur.right is None: 
                return d

            # If left child exists, add it to the level list with depth + 1
            if cur.left: 
                level.append((cur.left, d + 1))

            # If right child exists, add it to the level list with depth + 1
            if cur.right: 
                level.append((cur.right, d + 1))

        # If we've gone through all nodes without finding a leaf, return the last depth
        return depth