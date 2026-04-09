class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        m={}
        st=[]
        for i in range(len(nums)-1):
            st.append(nums[i])
        for i in range(len(nums)-1,-1,-1):
            while st and nums[i]>=st[-1]:
                from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        st = []
        
        # First pass: preload stack with elements for circularity
        for i in range(n - 1, -1, -1):
            st.append(nums[i])
        
        # Second pass: actual computation
        for i in range(n - 1, -1, -1):
            while st and st[-1] <= nums[i]:
                st.pop()
            if st:
                ans[i] = st[-1]
            else:
                ans[i] = -1
            st.append(nums[i])
        
        return ans
st.pop()
            
            if not st:
                m[nums[i]]=-1
            else:
                m[nums[i]]=st[-1]
            
            st.append(nums[i])
        
        return [m[x] for x in nums]