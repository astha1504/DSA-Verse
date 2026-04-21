class Solution:
    def numSubarraysWithSum(self, nums, goal: int) -> int:
        
        # atMost(goal)
        l=0
        sum=0
        cnt1=0
        for r in range(len(nums)):
            sum+=nums[r]
            while sum>goal:
                sum-=nums[l]
                l+=1
            cnt1+=(r-l+1)

        # if goal is 0 → directly return
        if goal==0:
            return cnt1

        # atMost(goal-1)
        l=0
        sum=0
        cnt2=0
        for r in range(len(nums)):
            sum+=nums[r]
            while sum>goal-1:
                sum-=nums[l]
                l+=1
            cnt2+=(r-l+1)

        return cnt1-cnt2