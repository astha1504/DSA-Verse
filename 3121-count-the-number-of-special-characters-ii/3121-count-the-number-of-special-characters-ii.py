class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}
        
        for i, ch in enumerate(word):
            if ch.islower():
                last_lower[ch] = i
            else:
                if ch not in first_upper:
                    first_upper[ch] = i
        
        cnt = 0
        for c in last_lower:
            C = c.upper()
            if C in first_upper and last_lower[c] < first_upper[C]:
                cnt += 1
        return cnt
