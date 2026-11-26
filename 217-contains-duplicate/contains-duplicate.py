class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        l = len(nums)
        x = set(nums)
        L = len(x)
        if l == L:
            return False
        else:
            return True