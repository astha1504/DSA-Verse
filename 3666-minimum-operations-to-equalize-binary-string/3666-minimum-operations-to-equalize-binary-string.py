class Solution:
    def minOperations(self, s: str, k: int) -> int:
        z=s.count('0')
        
        if z==0:
            return 0
        
        if k%2==0 and z%2==1:
            return -1
        
        if k>z and (k-z)%2==1:
            return -1
        
        if k==1:
            return z
        
        ans=(z+k-1)//k
        
        if (ans*k-z)%2!=0:
            ans+=1
        
        return ans