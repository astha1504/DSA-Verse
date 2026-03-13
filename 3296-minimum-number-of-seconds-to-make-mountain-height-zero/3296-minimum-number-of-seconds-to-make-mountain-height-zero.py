class Solution:
    def minNumberOfSeconds(self, h, wt):
        l, r = 0, max(wt) * h * (h + 1) // 2
        ans = r
        def ok(t):
            s = 0
            for w in wt:
                lim = 2 * t // w
                x = int((-1 + math.isqrt(1 + 4 * lim)) // 2)
                s += x
                if s >= h: return True
            return s >= h
        while l <= r:
            m = (l + r) // 2
            if ok(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans
