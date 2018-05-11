class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def isSym(p, q):
            if p and q:
                return (p.val == q.val and isSym(p.left, q.right) and isSym(p.right, q.left))
            return (p is q)

        return (isSym(root.left, root.right) if root else True)
