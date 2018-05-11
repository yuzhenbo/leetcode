# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # dfs recursively
    def levelOrderBottom1(self, root):
        res = []
        self.dfs(root, 0, res)
        return res
    def dfs(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.insert(0, [])
            res[-(level+1)].append(root.val)
            self.dfs(root.left, level+1, res)
            self.dfs(root.right, level+1 , res)

    # dfs + stack
    def levelOrderBottom2(self, root):
        stack = [(root, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))
        return res

    #bfs + queue

    def levelOrderBottom(self, root):
        queue, res = deque([(root, 0)]), []
        while queue:
            node, level = queue.popleft()
            if node:
                if len(res) < level+1:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        return res

    #改良版本
    def levelOrderBottom_1(self, root):
        queue, res = deque([(root, 0)]), []
        while queue:
            node, level = queue.popleft()
            if node:
                if level == len(res):
                    res.append([])
                res[level].append(node.val)
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        return res[::-1]

    def levelOrderBottom_2(self, root):
        res, queue = [], [root]
        while queue:
            res.append([node.val for node in queue if node])
            queue = [child for node in queue if node for child in (node.left, node.right)]
        return res[-2::-1]



a = TreeNode(3)
a.left = TreeNode(9)
a.right = TreeNode(20)
# a.left.left = TreeNode(None)
# a.left.right = TreeNode(None)
a.right.left = TreeNode(15)
a.right.right = TreeNode(7)

b = Solution().levelOrderBottom_2(a)
print(b)

