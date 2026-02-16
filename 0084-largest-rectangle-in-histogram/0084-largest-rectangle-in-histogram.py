class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st=[]
        ans=0
        h=heights
        h.append(0)
        for i in range(len(h)):
            while st and h[st[-1]]>h[i]:
                ht=h[st.pop()]
                w=i if not st else i-st[-1]-1
                ans=max(ans,ht*w)
            st.append(i)
        
        return ans
