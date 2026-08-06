# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #traverse the tree (root)
        #compare root with subRoot (sameTree)
        if not subRoot:
            return True
        if not root:
            return False 
        
        if self._same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)
    

    def _same_tree(self, q:Optional[TreeNode], p:Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self._same_tree(p.left,q.left) and self._same_tree(p.right,q.right)
        else:
            return False