class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_ocnt = 0
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                cnt = 0
            if cnt > max_ocnt:
                max_ocnt = cnt
        return max_ocnt