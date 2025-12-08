class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for a in range(1,n+1):
            for b in range(1,n+1):
                C=a*a+b*b
                c=int(C**0.5)
                if c*c==C and c<=n:
                    count+=1
        return count