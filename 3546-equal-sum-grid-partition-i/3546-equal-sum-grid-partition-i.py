class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m=len(grid)
        n=len(grid[0])
        rowsum=[0]*m
        colsum=[0]*n

        for i in range (m):
            for j in range (n):

                rowsum[i]+=grid[i][j]
                colsum[j]+=grid[i][j]
        if sum(rowsum)%2!=0:
            return False
        r=sum(rowsum)//2
        c=sum(colsum)//2
        a=0
        for i in rowsum:
            a+=i
            if a==r:
                return True
        a=0
        for i in colsum:
            a+=i
            if a==c:
                return True     
        return False       