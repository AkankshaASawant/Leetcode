# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        def pointer(l, r): 
            # Base case: if left index exceeds right index, return None
            if l > r: 
                return None
            
            # Calculate the middle index
            m = (l + r) // 2
            
            # Create a new TreeNode with the middle element as the root
            root = TreeNode(nums[m])
            
            # Recursively build the left subtree with elements before the middle
            root.left  = pointer(l, m - 1)
            
            # Recursively build the right subtree with elements after the middle
            root.right = pointer(m + 1, r)
            
            # Return the root of the current subtree
            return root
        
        # Start the recursion with the full range of the input array
        return pointer(0, len(nums) - 1)