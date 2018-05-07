class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for index, value in enumerate(nums):
            if value < target:
                continue
            return index
        return len(nums)

    def searchInsert1(self, nums, target):
        return len([x for x in nums if x<target])

    def searchInsert2(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low



Input = [1,3,5,6]


A = Solution()
B = A.searchInsert2(Input,7)
print(Input)
print(B)