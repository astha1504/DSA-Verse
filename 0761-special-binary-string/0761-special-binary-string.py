class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        sp=[]
        b=0
        st=0
        for i in range(len(s)):
            if s[i]=='1':
                b+=1
            else:
                b-=1

            if b==0:
                sp.append("1" + self.makeLargestSpecial(s[st + 1:i]) + "0")
                st=i+1

        sp.sort(reverse=True)
        return "".join(sp)