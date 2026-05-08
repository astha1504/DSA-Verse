from collections import deque, defaultdict
from typing import List

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        mx = max(nums)
        spf = [0]*(mx+1)
        for i in range(2, mx+1):
            if spf[i]==0:
                for j in range(i, mx+1, i):
                    if spf[j]==0: spf[j]=i

        def factors(x):
            f=[]
            while x>1:
                p=spf[x]
                f.append(p)
                while x%p==0: x//=p
            return f

        bucket=defaultdict(list)
        for i,v in enumerate(nums):
            for p in factors(v): bucket[p].append(i)

        vis=[0]*n
        vis[0]=1
        q=deque([(0,0)])

        while q:
            i,d=q.popleft()
            if i==n-1: return d
            for j in (i-1,i+1):
                if 0<=j<n and not vis[j]:
                    vis[j]=1;q.append((j,d+1))
            for p in factors(nums[i]):
                for j in bucket[p]:
                    if not vis[j]:
                        vis[j]=1;q.append((j,d+1))
                bucket[p].clear()
