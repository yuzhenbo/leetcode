from functools import reduce

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        int_digits = reduce(lambda x,y : 10*x +y, digits) + 1

        out = []
        for i in str(int_digits):
            out.append(i)

        return str(out)


Input = [1,3,4]

A = Solution()
B = A.plusOne(Input)

print(B)