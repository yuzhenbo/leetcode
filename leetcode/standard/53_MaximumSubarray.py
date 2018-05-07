class Solution:
    def maxSubArray(self, A):
        for i in range(1, len(A)):
            A[i] = max(A[i], A[i] + A[i - 1])
        return max(A)

Input = [-2, 1, 2, -5, 3, 4, -1]

A = Solution()
B = A.maxSubArray(Input)

print(B)