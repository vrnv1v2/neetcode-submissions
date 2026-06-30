# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.mv=0
        
        def depth(node,d):
            if not node:
                return
            self.mv=max(self.mv,d)
            depth(node.left,d+1)
            depth(node.right,d+1)
        
        
        depth(root,1)
        return self.mv
        
        

        