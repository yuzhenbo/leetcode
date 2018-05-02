class Solution(object):
    def reverse(self, x):

        if '-' not in str(x):
            x = [int(i) for i in list(str(x))]
            x = x[::-1]
            x = [str(i) for i in x]
            x = ''.join(x)
            x = int(x)

        else:
            x = str(x).strip('-')
            x = [int(i) for i in list((x))]
            x = x[::-1]
            x = [str(i) for i in x]
            x.insert(0, '-')
            x = ''.join(x)
            x = int(x)

        if (x >-2**31 and x<(2**31-1)):
            return x
        else:
            return 0

Input = 123

A = Solution()
B = A.reverse(Input)
print(B)