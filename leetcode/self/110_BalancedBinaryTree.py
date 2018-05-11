class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root):
        if not root:
            return 0
        d1 = self.dfs(root.left)

        if d1 == -1:
            return -1
        d2 = self.dfs(root.right)

        if d2 == -1:
            return  -1

        return -1 if abs(d1 - d2) > 1 else max(d1, d2) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root) != -1


a = TreeNode(3)
a.left = TreeNode(9)
a.right = TreeNode(20)
# a.left.left = TreeNode(None)
# a.left.right = TreeNode(None)
a.right.left = TreeNode(15)
a.right.right = TreeNode(7)

b = Solution().isBalanced(a)
print(b)

