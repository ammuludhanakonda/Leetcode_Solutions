class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        x = set(nums)
        k = len(x)
        s = list(x)
        s.sort()
        for i in range(len(nums) - k):
            s.append('_')
        nums[:] = s
        return k
        