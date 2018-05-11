class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        #这里有一个细节：如果不用［：］则会报错
        nums1[:] = sorted(nums1[0:m] + nums2[0:n])


a = [1,2,3,0,0,0]
b = [2,5,6]
m = 3
n = 3

A = Solution()
A.merge(a,3, b,3)
print(a)