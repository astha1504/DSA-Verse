class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD=10**9+7
        res=0
        for i in range(1, n+1):
            bits=i.bit_length()
            res=((res<<bits)+i)%MOD
        return res
