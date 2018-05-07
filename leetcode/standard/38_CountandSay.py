
from functools import reduce
class Solution(object):
    """ Quite straight-forward solution.
    We generate k-th string, and from k-th string we generate k+1-th string,
    until we generate n-th string.
    """
    ##方法一：比较难想
    def countAndSay(self, n):
        st = ['1']
        for k in range(1, n):
            st = list(map(str,
                     reduce(lambda x, y: x[:-2] + [x[-2] + 1] + [x[-1]] if x[-1] == y else x + [1, y], st, [0, st[0]])))
        return ''.join(st)

    ## 方法二：很清晰的递归思路

    def countAndSay1(self, n):
        if n == 1:
            return '1'

        return self.say(self.countAndSay1(n -1))

    def say(self, s):
        result = ''

        if not s:
            return ''

        count, digit = 1, s[0]

        for d in s[1:]:
            if d == digit:
                count += 1
            else:
                result += '{}{}'.format(count, digit)
                count, digit = 1, d
        result += '{}{}'.format(count, digit)
        return result


Input = 4


A = Solution()
B = A.countAndSay(Input)

print(B)

# from functools import reduce
# def func(x, y):
#     if x[-1] == y:
#         return x[:-2] + [x[-2] + 1] + [x[-1]]
#     else:
#         return x + [1, y]
# st = ['2','1']
# a = reduce(func, st , [0, st[0]])
# b = list(map(str, a))
# c = ''.join(b)
# print(c)
# reduce(func, [0, '1'],['1'])