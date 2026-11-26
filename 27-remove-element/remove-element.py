class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        cnt = 0
        r_cnt = 0
        l = []
        for i in range(len(nums)):
            if nums[i] != val:
                l.append(nums[i])
                cnt+= 1
        x = len(nums) - cnt
        for i in range(x):
            l.append('_')
        nums[:] = l
        return cnt