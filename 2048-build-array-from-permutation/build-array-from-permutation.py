class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        l = []
        for i in range(len(nums)):
            l.append(nums[nums[i]])
        return l

        