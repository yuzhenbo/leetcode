from functools import reduce
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x,y:x^y, nums)

if __name__ == '__main__':
    print(Solution().singleNumber([2, 4, 4, 2, 6]))