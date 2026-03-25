class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m=len(grid)
        n=len(grid[0])
        total=0
        rowsum=[0]*m
        colsum=[0]*n

        for i in range (m):
            for j in range (n):
                total+=grid[i][j]
                rowsum[i]+=grid[i][j]
                colsum[j]+=grid[i][j]
        if total%2!=0:
            return False

        upper=0
        for i in range (m-1):
            upper+=rowsum[i]
            if upper==total-upper:
                return True
        
        left=0
        for j in range (n-1):
            left+=colsum[j]
            if left==total-left:
                return True
        return False