class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        l = []
        for i in range(len(nums)):
            l.append(sum(nums[0:i+1]))
        return l