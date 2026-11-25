class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        s = set(nums)
        x = sorted(s)
        if len(x) == 1:
            return x[0]
        elif len(x) == 2:
            return x[1]
        else:
            return x[-3]

    