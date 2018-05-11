class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))