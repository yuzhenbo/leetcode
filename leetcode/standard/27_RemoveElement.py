class Solution:
    def removeElement(self, nums, val):
        for i in range(len(nums))[::-1]:
            if nums[i] == val:
                nums.pop(i)
        return len(nums)


Input = [3,2,2,3]


A = Solution()
B = A.removeElement(Input,3)
print(Input)
print(B)