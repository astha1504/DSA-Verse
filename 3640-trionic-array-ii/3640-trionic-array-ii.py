class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        INF = float('-inf')
        
        inc1 = nums[0]
        dec = INF
        inc2 = INF
        ans = INF
        
        for i in range(1, n):
            x = nums[i]
            prev = nums[i - 1]
            
            new_inc1 = x
            new_dec = INF
            new_inc2 = INF
            
            if prev < x:
                new_inc1 = inc1 + x
            
            if prev > x:
                new_dec = max(inc1 + x, dec + x)
            
            if prev < x:
                new_inc2 = max(dec + x, inc2 + x)
            
            inc1, dec, inc2 = new_inc1, new_dec, new_inc2
            ans = max(ans, inc2)
        
        return ans
