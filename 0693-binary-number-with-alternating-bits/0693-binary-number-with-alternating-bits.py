class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        xor=n^(n>>1)
        if (xor&(xor+1)==0):
            return True
        else:    
            return False    
            
