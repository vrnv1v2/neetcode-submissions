class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Start both stacks. We don't filter out None here because 
        # empty spaces are vital to checking structural identity.
        stack1 = [p]
        stack2 = [q]
        
        res1 = []
        res2 = []
        
        # 1. Serialize Tree 1 completely (including structure)
        while stack1:
            curr1 = stack1.pop()
            if not curr1:
                res1.append(None)  # Structural placeholder
                continue
                
            res1.append(curr1.val)
            # Push children regardless of whether they exist or are None
            stack1.append(curr1.right)
            stack1.append(curr1.left)
            
        # 2. Serialize Tree 2 completely
        while stack2:
            curr2 = stack2.pop()
            if not curr2:
                res2.append(None)  # Structural placeholder
                continue
                
            res2.append(curr2.val)
            stack2.append(curr2.right)
            stack2.append(curr2.left)
            
        # 3. If both structures and values match perfectly, they are identical
        return res1 == res2