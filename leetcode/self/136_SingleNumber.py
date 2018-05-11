class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = 0
        for num in nums:
            single ^= num
        return single

if __name__ == '__main__':
    print(Solution().singleNumber([2, 4, 4, 2, 6]))