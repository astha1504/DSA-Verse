class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows=len(strs)
        cols=len(strs[0])
        dele=0
        
        for i in range(cols):
            for j in range(1,rows):
                if strs[j][i]<strs[j-1][i]:
                    dele+=1
                    break
        return dele