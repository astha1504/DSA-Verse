class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo={}
        def lcs(i,j):
            if i==0 or j==0:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            
            if text1[i-1]==text2[j-1]:
                memo[(i,j)]=1+lcs(i-1,j-1)
            else:
                memo[(i,j)]=max(lcs(i-1,j),lcs(i,j-1))
            
            return memo[(i,j)]
        return lcs(len(text1),len(text2))