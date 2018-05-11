class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def depth(node):
            if not node:    #leaves
                return 0
            left = depth(node.left) #left child's depth
            right = depth(node.right) #right child's depth
            if abs(left-right)>1:
                raise Exception #stop recursion and report unbalance
            return max(left, right)+1
        try:
            return abs(depth(root.left)-depth(root.right))<=1
        except:
            return False