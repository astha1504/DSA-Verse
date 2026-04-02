class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1: return nums[0]
        
        def solve(arr):
            m=len(arr)
            dp=[0]*m
            dp[0]=arr[0]
            if m>1: dp[1]=max(arr[0],arr[1])
            for i in range(2,m):
                dp[i]=max(dp[i-1],dp[i-2]+arr[i])
            return dp[-1]
        return max(solve(nums[:-1]),solve(nums[1:]))
