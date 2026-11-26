class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        l = []
        l.append(0)
        for i in range(len(gain)):
            s = 0
            for j in range(i+1):
                s += gain[j]
            l.append(s)
        m = max(l)
        return m