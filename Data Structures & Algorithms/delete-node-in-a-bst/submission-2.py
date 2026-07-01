class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        curr = root
        parent = None

        # Step 1: Find the node and its parent
        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        # If key not found
        if not curr:
            return root

        # Step 2: Delete the node (Handle 3 cases)
        
        # Case A: Node to delete has at most 1 child
        if not curr.left or not curr.right:
            # Pick the existing child (or None if it's a leaf)
            child = curr.left if curr.left else curr.right
            
            # If we are deleting the root node itself
            if not parent:
                return child
            
            # Link parent to the child
            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child

        # Case B: Node to delete has 2 children
        else:
            # Find the inorder successor (smallest in the right subtree)
            succ_parent = curr
            succ = curr.right
            while succ.left:
                succ_parent = succ
                succ = succ.left
            
            # Replace current value with successor's value
            curr.val = succ.val
            
            # Delete the successor node (which can only have at most a right child)
            if succ_parent.left == succ:
                succ_parent.left = succ.right
            else:
                succ_parent.right = succ.right

        return root