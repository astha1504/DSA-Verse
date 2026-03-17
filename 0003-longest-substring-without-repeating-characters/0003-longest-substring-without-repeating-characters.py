class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp=[-1]*256
        l=0
        r=0
        ans=0
        total=0
        n=len(s)
        while(r<n):
            if mp[ord(s[r])]!=r:
                if mp[ord(s[r])]>=l:
                    l=mp[ord(s[r])]+1
            temp=r-l+1
            ans=max(temp,ans)
            mp[ord(s[r])]=r
            r+=1
        return ans           