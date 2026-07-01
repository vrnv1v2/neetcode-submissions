class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q) -> bool:
            stack1, stack2 = [p], [q]
            while stack1 and stack2:
                curr1 = stack1.pop()
                curr2 = stack2.pop()
                
                if not curr1 and not curr2:
                    continue
                if not curr1 or not curr2 or curr1.val != curr2.val:
                    return False
                    
                stack1.append(curr1.right)
                stack1.append(curr1.left)
                stack2.append(curr2.right)
                stack2.append(curr2.left)
            return len(stack1) == len(stack2)
        if not root:
            return False
        main=[root]
        while main:
            curr=main.pop()
            if curr.val==subRoot.val:
                if isSameTree(curr,subRoot):
                    return True
            if curr.left:
                main.append(curr.left)
            if curr.right:
                main.append(curr.right)
        return False