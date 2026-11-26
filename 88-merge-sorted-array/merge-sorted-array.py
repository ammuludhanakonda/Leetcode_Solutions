class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = []
        for i in range(m):
            l.append(nums1[i])
        x = l+nums2
        x.sort()
        nums1[:] = x