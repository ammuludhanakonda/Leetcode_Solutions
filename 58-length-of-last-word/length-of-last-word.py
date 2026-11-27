class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s[::-1]
        a = x.strip()
        cnt = 0
        for i in range(len(a)):
            if a[i] == ' ':
                break
            cnt += 1
        return cnt