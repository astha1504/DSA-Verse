class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9+7
        n=len(nums)
        dp=[0]*(n+1)
        pref=[0]*(n+1)
        dp[0]=pref[0]=1

        mn,mx=deque(),deque()
        left=0

        for right in range(n):
            while mn and nums[mn[-1]]>=nums[right]:
                mn.pop()
            mn.append(right)

            while mx and nums[mx[-1]]<=nums[right]:
                mx.pop()
            mx.append(right)

            while nums[mx[0]]-nums[mn[0]]>k:
                left += 1
                if mn[0]<left: mn.popleft()
                if mx[0]<left: mx.popleft()

            dp[right+1] = (pref[right] - (pref[left-1] if left else 0)) % MOD
            pref[right+1] = (pref[right] + dp[right+1]) % MOD

        return dp[n]
