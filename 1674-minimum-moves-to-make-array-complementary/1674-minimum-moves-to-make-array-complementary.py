from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0]*(2*limit+2)
        
        for i in range(n//2):
            a, b = nums[i], nums[n-1-i]
            diff[2] += 2
            diff[min(a,b)+1] -= 1
            diff[a+b] -= 1
            diff[a+b+1] += 1
            diff[max(a,b)+limit+1] += 1
        
        res = float('inf')
        cur = 0
        for s in range(2, 2*limit+1):
            cur += diff[s]
            res = min(res, cur)
        return res
