class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if target-num in d:
                return d[target-num]+1, i+1
            d[num]=i

nums = [2, 7, 11, 15]
target = 9
A = Solution()
B = A.twoSum(nums, target)
print(B)