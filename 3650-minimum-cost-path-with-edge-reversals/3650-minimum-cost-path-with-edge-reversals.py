class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        import heapq

        g = defaultdict(list)
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, 2 * w))

        dist = [float('inf')] * n
        dist[0] = 0
        pq = [(0, 0)]

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            if u == n - 1:
                return d
            for v, w in g[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))

        return -1
