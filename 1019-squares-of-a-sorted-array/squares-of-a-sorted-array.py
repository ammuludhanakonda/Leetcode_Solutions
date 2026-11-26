class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l = []
        for i in range(len(nums)):
            l.append(pow(nums[i] , 2))
        l.sort()
        return l