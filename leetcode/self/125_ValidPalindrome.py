import re
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub('[^a-zA-Z0-9]','',s)
        return s == s[::-1]

#击败了１００％