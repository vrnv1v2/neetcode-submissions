from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # The stack stores tuples: (node, lower_bound, upper_bound)
        # Python allows float('-inf') and float('inf') for clean boundary tracking
        stack = [(root, float('-inf'), float('inf'))]
        
        while stack:
            curr, low, high = stack.pop()
            
            # Check if the current node violates its strict path boundaries
            if not (low < curr.val < high):
                return False
            
            # Push the right child: lower bound updates to curr.val
            if curr.right:
                stack.append((curr.right, curr.val, high))
                
            # Push the left child: upper bound updates to curr.val
            if curr.left:
                stack.append((curr.left, low, curr.val))
                
        return True