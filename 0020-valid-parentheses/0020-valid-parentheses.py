class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mp = {')':'(',']':'[','}':'{'} 
        for ch in s:
            if ch in "([{":
                st.append(ch)
            else:
                if not st or st[-1]!=mp[ch]:
                    return False
                st.pop()
        return not st
