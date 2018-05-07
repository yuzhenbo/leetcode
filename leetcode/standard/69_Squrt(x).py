import numpy as np
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 牛顿迭代法
        r = x
        while r * r > x:
            r = (r + x / r) / 2
        return r

    def sqrt(self, x):
        if x == 0:
            return 0

        low = 1
        high = x
        mark = 1

        while low != high -1:
            mid = (high + low) // 2

            if mid * mid > x:
                high = mid
            elif mid * mid < x:
                mark = mid
                low = mid
            else:
                return mid
        return mark
