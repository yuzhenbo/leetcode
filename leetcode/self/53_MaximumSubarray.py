class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #最大子数列问题的目标是在数列的一维方向找到一个连续的子数列，使该子数列的和最大
        #Kadane算法扫描一次整个数列的所有数值，在每一个扫描点计算以该点数值为结束点的子数列的最大和（正数和）。
        # 该子数列由两部分组成：以前一个位置为结束点的最大子数列、该位置的数值。因为该算法用到了“最佳子结构”
        # （以每个位置为终点的最大子数列都是基于其前一位置的最大子数列计算得出），该算法可看成动态规划的一个例子。
        if not nums:
            return 0

        curSum = maxSum = nums[0]

        for num in nums[1:]:
            curSum = max(num, curSum+num)
            maxSum = max(maxSum, curSum)
        return maxSum




Input = [-2,1,2,-5,3,4,-1]


A = Solution()
B = A.maxSubArray(Input)

print(B)