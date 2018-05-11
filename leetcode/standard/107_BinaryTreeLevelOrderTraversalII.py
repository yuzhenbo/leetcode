# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        ans = []
        stack = [root]
        while stack:
            num = len(stack)
            tmp = []

            for i in range(num):
                m = stack.pop(0)
                if m.left:
                    stack.append(m.left)
                if m.right:
                    stack.append(m.right)
                tmp.append(m.val)

            ans.insert(0, tmp)
        return ans


a = TreeNode(3)
a.left = TreeNode(9)
a.right = TreeNode(20)
# a.left.left = TreeNode(None)
# a.left.right = TreeNode(None)
a.right.left = TreeNode(15)
a.right.right = TreeNode(7)

b = Solution().levelOrderBottom(a)
print(b)