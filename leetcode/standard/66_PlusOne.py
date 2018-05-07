class Solution:
    def plusOne(self, digits):
        return [int(i) for i in str(int(''.join(map(str, digits))) + 1)]