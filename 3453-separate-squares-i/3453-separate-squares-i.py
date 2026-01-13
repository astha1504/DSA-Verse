from typing import List
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        tot = sum(l*l for _, _, l in squares)
        tgt = tot / 2.0
        lo = min(y for _, y, _ in squares)
        hi = max(y+l for _, y, l in squares)

        for _ in range(100):
            mid = (lo + hi) / 2.0
            below = 0.0
            for _, y, l in squares:
                if mid <= y:
                    continue
                elif mid >= y+l:
                    below += l*l
                else:
                    below += l * (mid - y)
            if below < tgt:
                lo = mid
            else:
                hi = mid

        return (lo + hi) / 2.0
