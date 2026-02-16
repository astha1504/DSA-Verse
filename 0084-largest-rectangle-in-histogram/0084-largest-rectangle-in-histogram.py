class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        h=heights
        n=len(h)
        l=[0]*n
        r=[0]*n
        st=[]
        for i in range(n):
            while st and h[st[-1]]>=h[i]:
                st.pop()
            if st:
                l[i]=st[-1]
            else:
                l[i]=0
            st.append(i)
        
        st=[]
        for i in range(n-1,-1,-1):
            while st and h[st[-1]]>=h[i]:
                st.pop()
            if st:
                r[i]=st[-1]
            else:
                r[i]=n
            st.append(i)
        ans=0
        for i in range(n):
            w=r[i]-l[i]-1
            area=h[i]*w
            ans=max(ans,area)
        
        return ans
