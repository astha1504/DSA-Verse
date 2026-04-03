class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            cnt=bin(i)
            one=bin(i).count('1')
            ans.append(one)
        return ans