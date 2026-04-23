class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        has={}
        res=[0]*len(nums)
        for i in range(len(nums)):
            
            if nums[i] not in has:
                has[nums[i]]=[]
            has[nums[i]].append(i)
        for i in range(len(nums)):
            sums=0
            for j in has[nums[i]]:
                if i!=j:
                    sums+=abs(i-j)
            res[i]=sums
        return res


    