from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        if not nums:
            return [-1, -1]
        left,right=0,n
        while left<right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid
        start=left
        left,right=0,n
        while left<right:
            mid=(left+right)//2
            if nums[mid]<=target:
                left=mid+1
            else:
                right=mid
        end=left-1
        if start==n or nums[start]!=target:
            start=-1
        if end < 0 or nums[end]!=target:
            end=-1
        return [start,end]
