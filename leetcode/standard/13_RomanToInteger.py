class Solution:
    def romanToInt(self, s):
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num, pre = 0, 1000
        for i in [map[j] for j in s]:
            num, pre = num + i - 2 * pre if i > pre else num + i, i
        return num

Input = 'CDCM'

A = Solution()
B = A.romanToInt(Input)
print(B)