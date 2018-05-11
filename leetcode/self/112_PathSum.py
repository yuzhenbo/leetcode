class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        if root.left and self.hasPathSum(root.left, sum-root.val):
            return True
        if root.right and self.hasPathSum(root.right, sum - root.val):
            return True
        if not root.left and not root.right and sum == root.val:
            return True
        return False
