class Solution:
    def bestClosingTime(self, customers: str) -> int:
        t=customers.count('Y')
        p=0
        mn=float('inf')
        ans=0
        for j in range(len(customers)+1):
            penalty=(j-p)+(t-p)
            if penalty<mn:
                mn=penalty
                ans=j
            if j<len(customers) and customers[j]=='Y':
                p+=1
        return ans
