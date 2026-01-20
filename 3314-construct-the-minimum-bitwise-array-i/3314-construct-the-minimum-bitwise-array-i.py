from typing import List

class Solution:
    def minBitwiseArray(self,nums:List[int])->List[int]:
        ans=[]
        for p in nums:
            if p==2:
                ans.append(-1)
                continue
            k=0
            while(p>>k)&1:
                k+=1
            ans.append(p-(1<<(k-1)))
        return ans
