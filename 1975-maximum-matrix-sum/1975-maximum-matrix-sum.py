class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        s = 0
        m = float('inf')
        c = 0
        for r in matrix:
            for v in r:
                s += abs(v)
                m = min(m, abs(v))
                if v < 0:
                    c += 1
        if c % 2 == 0:
            return s
        return s - 2 * m
