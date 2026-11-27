class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        x = set(nums1)
        y = set(nums2)
        d1 = x - y
        a = len(d1)
        d2 = y - x
        b = len(d2)
        s = list(d1)
        t = list(d2)
        return [s,t]