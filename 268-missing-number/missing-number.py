class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        s = sum(nums)
        tot_sum = 0
        for i in range(0 , len(nums)+1 , 1):
            tot_sum += i
        return tot_sum - s