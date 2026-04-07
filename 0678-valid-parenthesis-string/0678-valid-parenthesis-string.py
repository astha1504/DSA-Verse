class Solution:
    def checkValidString(self, s: str) -> bool:
        openb = []
        aestric = []  
        for i in range(len(s)):
            if s[i] == '(':
                openb.append(i)
            elif s[i] == '*':
                aestric.append(i)
            else:
                if len(openb) != 0:
                    openb.pop()
                elif len(aestric) != 0:
                    aestric.pop()
                else:
                    return False
        while openb and aestric:
            if openb.pop() > aestric.pop():
                return False
                
        return len(openb) == 0