
#copy
class Solution(object):
    """ Quite straight-forward solution.
    We generate k-th string, and from k-th string we generate k+1-th string,
    until we generate n-th string.
    """
    def countAndSay(self, n):
        if n <= 1:
            return "1"

        pre_str = '1'
        for i in range(2, n+1):
            index = 0
            current_str = ''
            while index < len(pre_str):
                pos = index + 1


                repeat = 0
                while pos < len(pre_str) and pre_str[index] == pre_str[pos]:
                    pos += 1
                    repeat += 1

                current_str += str(repeat+1) + pre_str[index]

                index = pos
            pre_str = current_str
        return pre_str


Input = 4


A = Solution()
B = A.countAndSay(Input)

print(B)
