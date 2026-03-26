class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        dp_max = [[0] * n for _ in range(m)]
        dp_min = [[0] * n for _ in range(m)]
        
        dp_max[0][0] = dp_min[0][0] = grid[0][0]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                candidates = []
                if i > 0:
                    candidates.append(dp_max[i-1][j] * grid[i][j])
                    candidates.append(dp_min[i-1][j] * grid[i][j])
                if j > 0:
                    candidates.append(dp_max[i][j-1] * grid[i][j])
                    candidates.append(dp_min[i][j-1] * grid[i][j])
                dp_max[i][j] = max(candidates)
                dp_min[i][j] = min(candidates)
        
        result = dp_max[m-1][n-1]
        return result % MOD if result >= 0 else -1
