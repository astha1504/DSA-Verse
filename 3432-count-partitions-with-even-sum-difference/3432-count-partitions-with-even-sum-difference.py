class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ans=sum(nums)
        n=len(nums)
        if ans%2==0:
            return n-1
        return 0    
        
                