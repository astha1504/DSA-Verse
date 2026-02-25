from typing import List

class Solution:
    def largestTriangleArea(self, p: List[List[int]]) -> float:
        
        def ar(a, b, c):
            return abs(
                a[0]*(b[1]-c[1]) +
                b[0]*(c[1]-a[1]) +
                c[0]*(a[1]-b[1])
            ) / 2
        
        n = len(p)
        mx = 0.0
        
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    mx = max(mx, ar(p[i], p[j], p[k]))
        
        return mx