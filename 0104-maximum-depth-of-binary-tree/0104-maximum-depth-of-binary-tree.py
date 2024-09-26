# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        
#         if not root:            
#             return 0            # if the root is None, return None
        
#         # Recursive case:
#         # 1. Calculate the max depth of the left subtree
#         # 2. Calculate the max depth of the right subtree
#         # 3. Take the maximum of these two depths
#         # 4. Add 1 to account for the current node
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
          
#         if not root: 
#             return 0
        
#         level = 0
#         q = deque([root])
        
#         while q: 
#             for i in range(len(q)): 
#                 node = q.popleft()
#                 if node.left: 
#                     q.append(node.left)
#                 if node.right: 
#                     q.append(node.right)
#             level += 1
#         return level    
                
        stack = [[root, 1]]
        res = 0
        
        while stack: 
            node, depth = stack.pop()
            
            if node: 
                res = max(res, depth)
                stack.append([node.left, depth + 1]) 
                stack.append([node.right, depth + 1])
        return res        
                
    
        