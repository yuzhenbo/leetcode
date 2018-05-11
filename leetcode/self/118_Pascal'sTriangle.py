class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        nums = []
        for index in range(numRows):
            length = index + 1
            subnum = []
            for i in range(length):
                if i == 0 or i == length-1:
                    subnum.append(1)
                else:
                    subnum.insert(i, (nums[index-1][i-1] + nums[index-1][i]))

            nums.insert(index, subnum)

        return nums

Input = 5

A = Solution()
B = A.generate(Input)
print(B)
