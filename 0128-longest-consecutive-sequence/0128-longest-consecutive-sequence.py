class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans=0
        seen=set(nums)
        for num in seen:
            if num-1 not in seen:
                curr=num
                count=1
                while curr+1 in seen:
                    curr+=1
                    count+=1
                ans=max(count, ans)
        return ans