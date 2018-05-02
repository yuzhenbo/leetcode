class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = x if x > 0 else -x
        res = 0
        while n:
            res = res * 10 + n % 10
            n = n // 10 #python2的版本需要把这里的//变成/,注意区别
        if res > 0x7fffffff:
            return 0
        return res if x > 0 else -res


Input = 123

A = Solution()
B = A.reverse(Input)
print(B)