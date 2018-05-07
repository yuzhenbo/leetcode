class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = int(a, 2) + int(b, 2)
        return bin(c)[2:]

a = '11'
b = '1'

A = Solution()
B = A.addBinary(a, b)

print(B)