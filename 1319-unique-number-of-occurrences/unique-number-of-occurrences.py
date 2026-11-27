class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = {}
        for i in arr:
            freq[i] = freq.get(i , 0) + 1
        values = list(freq.values())
        s = set(values)
        if len(s) == len(values):
            return True
        else:
            return False