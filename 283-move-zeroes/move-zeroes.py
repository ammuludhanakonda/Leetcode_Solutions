class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = []
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                l.append(nums[i])
                cnt+= 1
        for i in range(len(nums)-cnt):
            l.append(0)
        nums[:] = l
        