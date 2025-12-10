class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        self.res=0
        def dfs(i):
            if i>=n: 
                return 0
            left=dfs(2*i+1)
            right=dfs(2*i+2)
            self.res+=abs(left-right)
            return cost[i]+max(left,right)
        dfs(0)
        return self.res
