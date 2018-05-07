class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #此题因为不允许开辟额外空间，所以不推荐使用删除重复元素。而选择将不重复元素放在原列表开头，返回新列表长度，截取原列表即可。
        if len(nums) == 0:
            return 0
        j = 0
        len_n = len(nums)
        for i in range(len_n):
            if nums[j] != nums[i]:
                nums[j + 1] = nums[i]
                j += 1
        return j + 1


Input = [1,1,2,3,3,3,4]

A = Solution()
B = A.removeDuplicates(Input)
print(B)