class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        INF = 10**18
        
        strs = set(original + changed)
        idx = {s: i for i, s in enumerate(strs)}
        m = len(idx)
        
        dist = [[INF] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0
        
        for o, c, w in zip(original, changed, cost):
            dist[idx[o]][idx[c]] = min(dist[idx[o]][idx[c]], w)
        
        for k in range(m):
            for i in range(m):
                for j in range(m):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        conv = {}
        for i in range(m):
            for j in range(m):
                if dist[i][j] < INF:
                    conv[(list(idx.keys())[i], list(idx.keys())[j])] = dist[i][j]
        
        dp = [INF] * (n + 1)
        dp[n] = 0
        
        for i in range(n - 1, -1, -1):
            if source[i] == target[i]:
                dp[i] = dp[i + 1]
            
            for l in range(1, n - i + 1):
                s_sub = source[i:i + l]
                t_sub = target[i:i + l]
                if s_sub in idx and t_sub in idx:
                    key = (s_sub, t_sub)
                    if key in conv:
                        dp[i] = min(dp[i], conv[key] + dp[i + l])
        
        return -1 if dp[0] == INF else dp[0]
