class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        p = []
        for i in range(len(nums)):
            s = 0
            for j in range(i+1):
                s += nums[j]
            p.append(s)
        nums.reverse()
        s = []
        for i in range(len(nums)):
            x = 0
            for j in range(i+1):
                x += nums[j]
            s.append(x)
        s.reverse()
        ind = 0
        fnd = 0
        for i in range(len(nums)):
            if p[i] == s[i]:
                fnd = 1
                ind = i
                break
        if fnd:
            return ind
        else:
            return -1