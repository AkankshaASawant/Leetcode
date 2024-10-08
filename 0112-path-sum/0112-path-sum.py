# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def dfs(node, curSum): 
            # Base case: if node is None, we can't find a path
            if not node: 
                return False 
            
            # Add current node's value to the running sum
            curSum += node.val
            
            # If it's a leaf node, check if the current sum equals the target sum
            if not node.left and not node.right: 
                return curSum == targetSum
            
            # Recursively check left and right subtrees
            # Return True if either subtree has a path with the target sum
            return (dfs(node.left, curSum) or 
                    dfs(node.right, curSum))
        
        # Start DFS from the root with initial sum of 0
        return dfs(root, 0)