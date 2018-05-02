class Solution:
    def isPalindrome(selfself, x):
        n = x if x > 0 else -x
        n_ago = n
        res = 0
        while n:
            res = res*10 + n%10
            n = n // 10

        if res > 0x7fffffff:
            return False
        else:
            n_now = res if x > 0 else -res

        if n_ago == n_now:
            return True
        else:
            return False