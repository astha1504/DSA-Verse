class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen=set()
        ans=2**k
        for i in range(len(s)-k+1):
            sub=s[i:i+k]
            seen.add(sub)
            if len(seen)==ans:
                return True
        return False