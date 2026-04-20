class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n=len(colors)
        maxi=0
        for i in range(n):
            for j in range(n):
                if colors[i]!=colors[j]:
                    ans=abs(i-j)
                    maxi=max(maxi,ans)
        return maxi