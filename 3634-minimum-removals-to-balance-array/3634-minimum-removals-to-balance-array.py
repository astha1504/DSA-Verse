class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        ans=n
        j=0

        for i in range(n):
            while j<n and nums[j]<=nums[i]*k:
                j+=1
            ans=min(ans,n-(j-i))   
        return ans    