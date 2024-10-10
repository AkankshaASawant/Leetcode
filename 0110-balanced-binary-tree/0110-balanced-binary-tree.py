# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def dfs(root):
            # Base case: if the node is None, it's balanced with height 0
            if not root:
                return [True, 0]
            
            # Recursively check left and right subtrees
            left, right = dfs(root.left), dfs(root.right)
            
            # Check if the current subtree is balanced:
            # 1. Both left and right subtrees are balanced
            # 2. The height difference between left and right is at most 1
            balanced = (left[0] and right[0] and
                        abs(left[1] - right[1]) <= 1)
            
            # Return whether the current subtree is balanced and its height
            return [balanced, 1 + max(left[1], right[1])]
        
        # Call the helper function and return whether the whole tree is balanced
        return dfs(root)[0]