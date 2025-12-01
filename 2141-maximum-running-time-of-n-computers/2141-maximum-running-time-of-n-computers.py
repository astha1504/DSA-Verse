class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total=sum(batteries)
        l=0
        r=total//n
        def run(T):
            c=0
            for b in batteries:
                if b<T:
                    c+=b
                else:
                    c+=T
            req=n*T
            return c>=req
        while l<r:
            mid=(l+r+1)//2
            if run(mid):
                l=mid
            else:
                r=mid-1
        return l
                                