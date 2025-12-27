import heapq

class Solution:
    def mostBooked(self,n:int,meetings:List[List[int]])->int:
        meetings.sort()
        avail=list(range(n))
        heapq.heapify(avail)
        ongoing=[]
        cnt=[0]*n
        for s,e in meetings:
            while ongoing and ongoing[0][0]<=s:
                t,r=heapq.heappop(ongoing)
                heapq.heappush(avail,r)
            if avail:
                r=heapq.heappop(avail)
                heapq.heappush(ongoing,(e,r))
                cnt[r]+=1
            else:
                t,r=heapq.heappop(ongoing)
                d=e-s
                ne=t+d
                heapq.heappush(ongoing,(ne,r))
                cnt[r]+=1
        m=max(cnt)
        for i in range(n):
            if cnt[i]==m:
                return i
