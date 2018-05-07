class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_len = len(needle)
        if needle_len == 0:
            return 0

        for i, character in enumerate(haystack):
            if haystack[i:i + needle_len] == needle:
                return i

        return -1