class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1


Input = 'helloll'
Input1 = 'll'


A = Solution()
B = A.strStr(Input,Input1)
print(Input)
print(B)