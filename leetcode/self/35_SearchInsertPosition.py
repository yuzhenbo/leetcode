class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            for i, j in enumerate(nums):
                if nums[-1] < target:
                    return len(nums)
                elif nums[0] > target:
                    return  0
                elif nums[i] < target and nums[i+1] > target:
                    return i + 1



Input = [1,3,5,6]


A = Solution()
B = A.searchInsert(Input,7)
print(Input)
print(B)