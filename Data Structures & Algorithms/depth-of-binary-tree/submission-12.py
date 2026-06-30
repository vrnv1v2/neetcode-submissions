# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue=deque([(root,1)])
        mv=0
        while queue:
            curr,d=queue.popleft()
            mv=max(mv,d)
            if curr.left:
                queue.append((curr.left,d+1))
            if curr.right:
                queue.append((curr.right,d+1))
        return mv
        
        

        