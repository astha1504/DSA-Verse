class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[]

        for i in range(m+1):
            row=[]
            for j in range(n+1):
                row.append(0)
            dp.append(row)

        for i in range(1,m+1):
            for j in range(1,n+1):

                if text2[i-1]==text1[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]

                else:
                    if dp[i-1][j]>dp[i][j-1]:
                        dp[i][j]=dp[i-1][j]
                    else:
                        dp[i][j]=dp[i][j-1]

        return dp[m][n]