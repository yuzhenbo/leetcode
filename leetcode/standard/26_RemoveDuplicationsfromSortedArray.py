class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums) - 1)[::-1]:
            if nums[i] == nums[i + 1]:
                nums.pop(i)


Input = [1,1,2,3,3,3,4]

A = Solution()
B = A.removeDuplicates(Input)
print(B)