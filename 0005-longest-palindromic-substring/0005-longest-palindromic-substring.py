class Solution:
    def longestPalindrome(self, s: str) -> str:
        def find(l,r):
            while l>=0 and r<len(s):
                if s[l]==s[r]:
                    l-=1
                    r+=1
                else:
                    break
            return s[l+1:r]
        n=len(s)
        ans=""

        for i in range(n):
            len1=find(i,i)
            len2=find(i,i+1)
            if len(ans)<len(len1):
                ans=len1
            if len(ans)<len(len2):
                ans=len2
        return ans