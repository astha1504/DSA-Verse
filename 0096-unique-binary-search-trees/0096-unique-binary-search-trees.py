class Solution:
    def numTrees(self, n: int) -> int:
        #case 1 empty tree res=1
        #case 2 ek node res=1
        #case 3 1->2 or 2->1 res=2
        dp=[1]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range (2,n+1):
            total=0
            for j in range(1,i+1):
                total+=dp[j-1]*dp[i-j]
            dp[i]=total    
        return dp[n]        
