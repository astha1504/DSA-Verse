class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict=set(wordDict)  
        memo={}           
        def helper(idx):
            if idx==len(s):
                return True
            if idx in memo:
                return memo[idx]
            
            for i in range(idx+1,len(s)+1):
                if s[idx:i] in wordDict and helper(i):
                    memo[idx]=True
                    return True
            
            memo[idx]=False
            return False
        
        return helper(0)