class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        st, en = 0, 0
        def f(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1
        for i in range(len(s)):
            l1, r1 = f(i, i)
            l2, r2 = f(i, i + 1)
            if r1 - l1 > en - st:
                st, en = l1, r1
            if r2 - l2 > en - st:
                st, en = l2, r2
        return s[st:en+1]
