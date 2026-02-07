class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp=0
        countb=0
        for ch in s:
            if ch=='a':
                dp=min(dp+1,countb)
            else:
                countb+=1
        return dp            