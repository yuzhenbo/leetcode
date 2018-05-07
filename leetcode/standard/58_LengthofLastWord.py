class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split()
        return len(l[-1]) if l else 0


Input = 'hellow world   '

A = Solution()
B = A.lengthOfLastWord(Input)

print(B)