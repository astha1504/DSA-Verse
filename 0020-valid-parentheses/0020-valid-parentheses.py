class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        n=len(s)
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                st.append(ch)
            else:
                if not st:
                    return False
                else:
                    top=st.pop()
                    if (ch == ')' and top != '(') or (ch == '}' and top != '{') or(ch == ']' and top != '['):
                        return False

        return len(st)==0