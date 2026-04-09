class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m={}
        st=[]
        
        for i in range(len(nums2)-1,-1,-1):
            while st and nums2[i]>=st[-1]:
                st.pop()
            
            if not st:
                m[nums2[i]]=-1
            else:
                m[nums2[i]]=st[-1]
            
            st.append(nums2[i])
        
        return [m[x] for x in nums1]