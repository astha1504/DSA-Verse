class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD=10**9+7
        yc=Counter(y for _, y in points)
        c=[]
        for v in yc.values():
            if v>=2:
                c.append(v*(v-1)//2)
        s=sum(c)%MOD
        sq=sum((x*x) % MOD for x in c) % MOD
        ans=(s*s-sq) % MOD
        ans=(ans*pow(2, MOD-2,MOD))%MOD  
        return ans