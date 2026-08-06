
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        #Have to use the tuple swap here, can't separate to different line. 
        #otherwise we will lose reference to the child node value 
        root.left, root.right = root.right, root.left
        #pre-order traverse 
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root