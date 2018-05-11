class Solution:
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))]
        # 注意这里是为了防止第一个出错
        return res[:numRows]

    def generate1(self, numRows):
        resultset = [[1] * (i + 1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i):
                resultset[i][j] = resultset[i - 1][j - 1] + resultset[i - 1][j]

        return resultset




Input = 5

A = Solution()
B = A.generate1(Input)
print(B)
