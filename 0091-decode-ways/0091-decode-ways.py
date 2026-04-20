class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        if s[0]=='0' or n==0:
            return 0
        memo={}
        def helper(i):
            count=0
            if i==n:
                return 1
            
            if s[i]=='0':
                return 0
            if i in memo:
                return memo[i]
                
            count=helper(i+1)
            if i+1<n and 10<= int(s[i:i+2])<27:
                count+=helper(i+2)
            memo[i]=count
            return count
        return helper(0)