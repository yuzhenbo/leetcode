class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        else:

            return len(s.strip().split(' ')[-1])



Input = 'hellow world '

A = Solution()
B = A.lengthOfLastWord(Input)

print(B)