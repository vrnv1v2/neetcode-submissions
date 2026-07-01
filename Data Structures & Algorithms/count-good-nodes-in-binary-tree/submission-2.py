# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        mv=0
        stack=[(root,root.val)]
        count=0
        while stack:
            curr,m=stack.pop()
            if curr.val>=m:
                m=curr.val
                count+=1

            if curr.right:
                stack.append((curr.right,m))
            if curr.left:
                stack.append((curr.left,m))
        return count
        
        


        
        